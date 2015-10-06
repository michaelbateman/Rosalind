

import numpy as np

s = 'rosalind_deg.txt'

with open(s, 'r') as input_file:
	#lines = input_file.readlines()
	#temp = lines[0].strip()
	#temp2 = temp.split()
	#n = int(temp2[0])
	#m = int(temp2[1])
	#for i in range(1, 1 + n):
		#lines[i]
	
	n,m = [int(x) for x in input_file.readline().split()]
	#print n
	#print m
	ctr = [0] * n
	
	#print ctr
	
	for line in input_file:
		#temp = line.strip()
		a,b = [int(x) for x in line.split()]
		#print a
		#print b
		ctr[a-1] +=1
		ctr[b-1] +=1
		

for i in range(0, n):
	print ctr[i],

