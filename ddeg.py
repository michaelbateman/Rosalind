

import numpy as np

s = 'rosalind_ddeg.txt'

neigh = {}


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
	deg = [0] * n
	
	for i in range(0, n):
		neigh.update({i:[]})
	
	
	
	#print ctr
	
	for line in input_file:
		#temp = line.strip()
		a,b = [int(x) for x in line.split()]
		#print a
		#print b
		deg[a-1] +=1
		deg[b-1] +=1
		neigh[a-1].append(b-1)
		neigh[b-1].append(a-1)

for i in range(0, n):
	#print neigh[i]
	total = 0 
	for j in neigh[i]:
		total += deg[j]
	print total,
