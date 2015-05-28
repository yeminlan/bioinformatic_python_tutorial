#!/usr/bin/env python
#translate nucleotides to proteins, assuming each read takes two lines (header & seq)

import sys
import re

dict = {'GCT':'A','GCC':'A','GCA':'A','GCG':'A','CGT':'R','CGC':'R','CGA':'R','CGG':'R', \
		'AGA':'R','AGG':'R','AAT':'N','AAC':'N','GAT':'D','GAC':'D','TGT':'C','TGC':'C', \
		'CAA':'Q','CAG':'Q','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G', \
		'CAT':'H','CAC':'H','ATT':'I','ATC':'I','ATA':'I','TTA':'L','TTG':'L','CTT':'L', \
		'CTC':'L','CTA':'L','CTG':'L','AAA':'K','AAG':'K','ATG':'M','TTT':'F','TTC':'F', \
		'CCT':'P','CCC':'P','CCA':'P','CCG':'P','TCT':'S','TCC':'S','TCA':'S','TCG':'S', \
		'AGT':'S','AGC':'S','ACT':'T','ACC':'T','ACA':'T','ACG':'T','TGG':'W','TAT':'Y', \
		'TAC':'Y','GTT':'V','GTC':'V','GTA':'V','GTG':'V','TAA':'*','TGA':'*','TAG':'*'}

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'w+')

for line in f1.readlines():
	if line[0]=='>':
		header = line
	else:
		#translate
		ind = xrange(0,len(line)-3,3)
		seq = ''
		for j in ind:
			seq += dict[line[j:j+3]]
		#substring between start and stop, assuming there's 0 or 1 protein per read
		r = re.search("M(\w)+\*",seq)
		if r:
			f2.write(header)
			f2.write(r.group(0)[:-1]+'\n')

f1.close()
f2.close()


