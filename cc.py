#Given: A simple graph with n<=1000 vertices in the edge list format.

#Return: The number of connected components in the graph.

import numpy as np
import sys
sys.setrecursionlimit(10000)

#def add_new(k, neigh, L):
	#for j in neigh[k]:
		#if j not in path:


#def find_comp(i, neigh): # finds the connected component containing i
	#path = [i]
	#j = 0
	#current = i
	#done = 0
	#while done == 0:
		#while j < len(neigh[current])
			#if neigh[current][j] not in path:
				#current = neigh[current][j]
				#path.append[current]
				#break
			#elif j == len(neigh[current]) - 1: 
				
				#j +=1
			
		
		


def explore(v, neigh, visited, precursor):
	#print visited
	#print precursor
	#print neigh[v]
	if len(neigh[v]) == 0:
		return visited
	
	for u in neigh[v]:
		#print u
		#print visited
		if u not in visited:
			#print 'hello'	
			
			visited.append(u)
			precursor.append(v)
			explore(u, neigh, visited, precursor)
		
	if len(precursor) == 1:
		return visited
	else:
		#print 'a;ldskfj'
		#print visited
		#print precursor
		#print v
		return explore(precursor[-1], neigh, visited, precursor[:-1])



s = 'rosalind_cc.txt'
neigh = {}

with open(s, 'r') as input_file:

	n,m = [int(x) for x in input_file.readline().split()]
	deg = [0] * n
	for i in range(0, n):
		neigh.update({i:[]})
	
	for line in input_file:
		a,b = [int(x) for x in line.split()]
		neigh[a-1].append(b-1)
		neigh[b-1].append(a-1)

comp_dict = {}

comp_ctr = 0

for i in range(0, n):
	new_comp = 1
	for j in range(0, len(comp_dict)):
		#print j, 'comp dict = ', comp_dict[j]
		if i in comp_dict[j]:
			comp_dict.update({i:comp_dict[j]})
			new_comp = 0
	if new_comp ==0: pass
	else:			
		L = explore(i, neigh, [i], [])
		print L
		comp_dict.update({i:explore(i, neigh, [i], [])})
		comp_ctr +=1
	
print comp_ctr