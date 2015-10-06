#Given: k graphs in edge/list format

#Return: 1 if the graph has nontrivial 4-cycle, -1 else

import numpy as np
import sys
sys.setrecursionlimit(10000)


		
def has_square(neigh): # returns 1 if graph given by neigh structure has 4-cycle, -1 otherwise
	trivial = [0] *len(neigh)
	for k in neigh.keys():
		total = 0
		for l in neigh[k]:
			total+=len(neigh[l]) - 1
		trivial[k] = total + len(neigh[k])**2
		#print k, trivial[k]
	
	
	N = len(neigh)
	x = np.arange(N**2).reshape(N,N)
	A = np.matrix(x)
	for i in range(0, N):
		for j in range(0,N):
			#print i, j, np.shape(A)
			#print A[i,j]
			if i in neigh[j]: A[i,j] = 1
			else: A[i,j] = 0
	b = np.linalg.matrix_power(A, 4)
	#for row in b:
		#for val in row:
			
			#print val,
		#print
	#print
	for j in neigh.keys():
		if b[j,j] -  trivial[j] >0: return 1
	#	print  b[j,j] -  trivial[j],
	#print
	return -1

filename = 'rosalind_sq.txt'


new_graph = 0 
neigh = {}
ctr = 0 
with open(filename, 'r') as input_file:
	
	num_graphs = [int(x) for x in input_file.readline().split()]
	num_graphs =  num_graphs[0]
	#print num_graphs
	#ans = [0] * num_graphs
	for line in input_file:
		if len(line.strip()) == 0:
			
			if ctr > 0: 
				print has_square(neigh),
				
			neigh = {}	
			new_graph= 0
			
		elif new_graph == 0:
			ctr +=1
			s = line.strip()
			n, m = line.split()
			n = int(n)
			new_graph = 1
			for i in range(0, n):
				neigh.update({i:[]})
		else:
			ctr +=1
			a,b = [int(x) for x in line.split()]
			neigh[a-1].append(b-1)
	                neigh[b-1].append(a-1)


	print has_square(neigh)


#for a in neigh.keys():
	#print a, neigh[a]

	

