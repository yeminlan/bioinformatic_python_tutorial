#!/usr/bin/env python

import sys
from Bio import SeqIO
from Bio import SearchIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC
# from Bio import Entrez
# from Bio.Blast import NCBIWWW
# from Bio.Blast import NCBIXML


#01. concatenate R1 and R3 file
f1 = open('testR1.fastq','r')
f2 = open('testR3.fastq','r')
f3 = open('concatenate.fastq','w+')
seqs1 = list(SeqIO.parse(f1,"fastq"))
seqs2 = list(SeqIO.parse(f2,"fastq"))
ind = xrange(0,len(seqs1),1)
seqs3 = []
for i in ind: seqs3.append(seqs1[i] + seqs2[i])
SeqIO.write(seqs3,f3,"fastq")
f1.close()
f2.close()
f3.close()
del f1,f2,f3,seqs1,seqs2,ind,i

#02. extract reads whose barcode start with A or T (barcode file testR2.fastq) 
f4 = open('testR2.fastq','r')
f5 = open('extract.fasta','w+')
seqs4 = list(SeqIO.parse(f4,"fastq"))
ind = filter(lambda s: s.seq[0]=="A" or s.seq[0]=="T", seqs4)
ids = []
for i in ind: ids.append(i.id)
seqs5 = filter(lambda s: s.id in ids, seqs3)
SeqIO.write(seqs5,f5,"fasta") #03. convert fastq to fasta file 
f4.close()
f5.close()
del f4,f5,seqs3,seqs4,ind,ids,i

#04. delete N's in fasta file
f6 = open('removeN.fasta','w+')
seqs6 = []
for s in seqs5:
    seqs6.append(SeqRecord(s.seq.ungap(gap="N"),id=s.id,name='',description=''))
SeqIO.write(seqs6,f6,"fasta") 
f6.close()
del f6,s,seqs5

#05. format fasta file so that each read takes two lines (header & seq)
f7 = open('format.fasta','w+')
seqs7 = seqs6
writer = SeqIO.FastaIO.FastaWriter(f7, wrap=0)
writer.write_file(seqs7)
f7.close()
del f7,seqs6,writer

#06. count number of bases for each read, output a tab-separated values (TSV) file
f8 = open('countbase.tsv','w+')
for s in seqs7:
    f8.write(">"+s.id+"\t"+str(len(s.seq))+"\n")
f8.close()
del s,f8

#07. get reverse complement seqs for nucleotides
f9 = open('revcom.fasta','w+')
seqs9 = []
for s in seqs7:
    seqs9.append(SeqRecord(s.seq.reverse_complement(),id=s.id,name='',description=''))
writer = SeqIO.FastaIO.FastaWriter(f9,wrap=0)
writer.write_file(seqs9)
f9.close()
del f9,s,writer,seqs7

#08. translate the nucleotides to proteins
f10 = open('translate.faa','w+')
seqs10 = []
for s in seqs9:
    seqs10.append(SeqRecord(s.seq.translate(),id=s.id,name='',description=''))
writer = SeqIO.FastaIO.FastaWriter(f10,wrap=0)
writer.write_file(seqs10)
f10.close()
del f10,s,writer,seqs9

