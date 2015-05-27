#!/usr/bin/env python
# extract from fastq file to keep reads whose barcode start with A or T, assuming fastq files are in the same order

import sys
import re

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'r')
fo = open(sys.argv[3],'w+')

while True:
	f2.readline()
	line = f2.readline()
	if line:
		if re.search('^(A|T)',line):
			fo.write(f1.readline())
			fo.write(f1.readline())
			fo.write(f1.readline())
			fo.write(f1.readline())
		else:
			f1.readline()
			f1.readline()
			f1.readline()
			f1.readline()
		f2.readline()
		f2.readline()
	else:
		break

f1.close()
f2.close()
fo.close()


