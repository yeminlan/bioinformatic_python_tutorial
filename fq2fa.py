#!/usr/bin/env python
# convert fastq to fasta

import sys

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'w+')

while True:
	line = f1.readline()
	if line:
		f2.write('>'+line[1:])
		f2.write(f1.readline())
		f1.readline()
		f1.readline()
	else:
		break

f1.close()
f2.close()


