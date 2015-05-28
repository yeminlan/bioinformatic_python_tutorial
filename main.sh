#!/bin/bash

#01. concatenate R1 and R3 file
python concatenate.py testR1.fastq testR3.fastq concatenate.fastq

#02. extract reads whose barcode start with A or T (barcode file testR2.fastq) 
python extract.py concatenate.fastq testR2.fastq extract.fastq

#03. convert fastq to fasta file 
python fq2fa.py extract.fastq extract.fasta

#04. delete N's in fasta file
python removeN.py extract.fasta removeN.fasta

#05. format fasta file so that each read takes two lines (header & seq)
#note fasta file converted from fastq usually won't need this step
python format.py removeN.fasta format.fasta

#06. count number of bases for each read, output a tab-separated values (TSV) file
python countbase.py format.fasta countbase.tsv

#07. get reverse complement seqs for nucleotides
python revcom.py format.fasta revcom.fasta

#08. translate the nucleotides to proteins
python translate.py revcom.fasta translate.faa

