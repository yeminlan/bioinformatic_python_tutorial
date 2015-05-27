#!/usr/bin/env python
#format fasta file so that each read takes two lines (header & seq)

import sys

f1 = open(sys.argv[1],'r')
f2 = open(sys.argv[2],'w+')

initial_flag = 1
for line in f1.readlines():
	if line[0]==">":
		if initial_flag==1:
			f2.write(line)
			initial_flag = 0
		else:
			f2.write('\n'+line)
	else:
		f2.write(line[0:-1])

f2.write('\n')

f1.close()
f2.close()


