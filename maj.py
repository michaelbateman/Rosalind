

import numpy as np

s = 'rosalind_maj.txt'



def majority(A):
	for m in A:
		if A.count(m) > len(A)/2:
			return m
	return -1
	





with open(s, 'r') as input_file:
	#lines = input_file.readlines()
	#temp = lines[0].strip()
	#temp2 = temp.split()
	#n = int(temp2[0])
	#m = int(temp2[1])
	#for i in range(1, 1 + n):
		#lines[i]
	
	k,n = [int(x) for x in input_file.readline().split()]
	
	
	for line in input_file:
		A= [0] * n
		A = [int(x) for x in line.split()]
		print majority(A),
