#!/usr/bin/env python
# concatenate forward and reverse fastq files into one fastq file with longer reads, assuming the same order

import sys
import re

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'r')
fo = open(sys.argv[3],'w+')

while True:
	line = f1.readline()
	if line:
		header = re.search('(\S)+',line)
		fo.write(header.group(0)+'\n')
		fo.write(f1.readline()[:-1])
		rr = f2.readline()
		rr = f2.readline()
		fo.write(rr)
		fo.write(f1.readline())
		fo.write(f1.readline()[:-1])
		rr = f2.readline()
		rr = f2.readline()
		fo.write(rr)
	else:
		break

f1.close()
f2.close()
fo.close()


