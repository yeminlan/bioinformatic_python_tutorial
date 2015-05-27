#!/usr/bin/env python
#count number of bases for each read, output a tab-separated values (TSV) file
#fasta file doesn't need to be two-line (header & seq) format

import sys

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'w+')

for line in f1.readlines():
	if line[0]==">":
		if 'c' in locals():
			f2.write(str(c)+'\n')
		f2.write(line[1:-1]+'\t')
		c = 0
	else:
		c += len(line)-1
		
f2.write(str(c)+'\n')

f1.close()
f2.close()
