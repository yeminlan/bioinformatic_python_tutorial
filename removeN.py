#!/usr/bin/env python
# remove N's in fasta file

import sys

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'w+')

while True:
	line = f1.readline()
	if line:
		f2.write(line)
		line = f1.readline()
		f2.write(line.replace('N',''))
	else:
		break

f1.close()
f2.close()

