#Given: A simple graph with n<=1000 vertices in the edge list format.

#Return: The number of connected components in the graph.

import numpy as np
import sys
sys.setrecursionlimit(10000)



def bubble(A, M):
	A.append(M)
	i = len(A) - 1
	#parent = (i + 1) / 2 - 1
	while A[(i + 1) / 2 - 1] < A[i] and i > 0:
		temp = A[i]
		A[i] = A[(i + 1) / 2 - 1]
		A[(i + 1) / 2 - 1] = temp
		i = (i + 1) / 2 - 1
	return A



s = 'rosalind_hea.txt'

with open(s, 'r') as input_file:

	temp = input_file.readline()
	n = temp.strip()
	for line in input_file:
		A = [int(x) for x in line.split()]
	#print n 
	#print A

B = [A[0]]

for i in range(1, len(A)):
	B = bubble(B, A[i])
	

for i in range(0, len(A)):
	print B[i],
