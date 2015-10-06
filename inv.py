#Given: an integer n and array of length n

#Return: number of inversions in array

import numpy as np
import sys
sys.setrecursionlimit(10000)



def make_rand_array(n):
	return np.random.randint(low = -10000, high = 10000, size = n)
	

def num_inv(C): # returns number of inversions in arary C, using naive pairwise comparison
	ctr = 0
	for i in range(0, len(C)):
		if i 
		for j in range(i+1, len(C)):
			if C[i] > C[j]:
				ctr +=1
			else:
				pass
	return ctr


s = 'rosalind_inv.txt'
neigh = {}
edges = {}
ctr = 0
new_graph = 0



with open(s, 'r') as input_file:

	for line in input_file:
		temp = line.strip()
		#print temp.split()
		if len(temp.split()) == 1:
			pass
		else:
			A = [int(x) for x in temp.split()]
		
		
		
B = make_rand_array(10000)
print num_inv(A)
#print num_inv(B)
