#Given: a list of graphs

#Return: +1 if it contains a negative weight cycle, -1 otherwise.  (use bellman-ford, as in bf.py)

import numpy as np
import sys
sys.setrecursionlimit(10000)


			
			
def neg_weight_cycle(neigh,edges):
	dist = [0]*len(neigh)
	unreachable = []
	visited = []
	unvisited = neigh.keys()
	for j in neigh.keys():
		if j ==0:
			dist[j] = 0
		else:
			dist[j] = 'inf'
						
	ind = 1
	for i in range(0, len(neigh) -1):
		for (u,v) in edges:
			if dist[u] == 'inf':
				temp = 'inf'
			else:
				temp = edges[(u,v)] + dist[u]
			if temp < dist[v]:
				dist[v] = temp
			else:
				pass
		#print ind
		ind +=1	
	
	for (u,v) in edges:
		if dist[u] == 'inf':
			temp = 'inf'
		else:
			temp = edges[(u,v)] + dist[u]
		if temp < dist[v]:
			return 1
			dist[v] = temp
		else:
			pass
	for j in neigh.keys():
		if dist[j] == 'inf':
			unreachable.append(j)
	return unreachable
	

s = 'rosalind_nwc.txt'
neigh = {}
edges = {}
ctr = 0
new_graph = 0
with open(s, 'r') as input_file:
	
	#num_graphs = [int(x) for x in input_file.readline().split()]
	#num_graphs =  num_graphs[0]
	#print num_graphs
	#ans = [0] * num_graphs
	for line in input_file:
		temp = line.strip()
		#print len(temp.split())
		if len(temp.split()) == 0:
			pass
		elif len(temp.split()) == 1:
			num_graphs = temp[0]
		elif len(temp.split()) == 2:
			if ctr > 0: 
				ans = neg_weight_cycle(neigh, edges)
				if ans == 1:
					print ans,
				else:
					while len(ans) > 0:
					ans = neg_weight_cycle(neigh, edges)	
					
			neigh = {}
			edges = {}	
			new_graph= 0
			n,m = temp.split()
			n = int(n)
			#print 'n is', n
			new_graph = 1
			for i in range(0, n):
				neigh.update({i:[]})
			ctr +=1
			
		
		
		#elif new_graph == 0:
			#ctr +=1
			#s = line.strip()
			#n, m = line.split()
			#n = int(n)
			#new_graph = 1
			#for i in range(0, n):
				#neigh.update({i:[]})
		else:
			#print 'neigh', len(neigh)
			ctr +=1
			a,b, w = [int(x) for x in line.split()]
			neigh[a-1].append(b-1)
	                #neigh[b-1].append(a-1)
			edges.update({(a-1, b-1):w}) # this gives us the weight of the edge (a-1, b-1)
						# definitely poor naming, should be 'weights' or something

	print neg_weight_cycle(neigh, edges)

