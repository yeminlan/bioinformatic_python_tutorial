#!/usr/bin/env python
#get reverse complement DNA seqs for nucleotides

import sys

dict = {'A':'T','G':'C','C':'G','T':'A'}

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'w+')

for line in f1.readlines():
	if line[0]=='>':
		f2.write(line)
	else:
		ind = xrange(len(line)-2,-1,-1) #note the last char is end-of-line
		seq = ''
		for i in ind:
			seq += dict[line[i]]
		f2.write(seq+'\n')

f1.close()
f2.close()


