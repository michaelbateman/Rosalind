#Given: a list of graphs

#Return: +1 if it contains a negative weight cycle, -1 otherwise.  (use bellman-ford, as in bf.py)

import numpy as np
import sys
sys.setrecursionlimit(10000)


			
		
def find_min(V, d):
	m = 'inf'
	j_min = V[0]
	for j in V:
		if d[j] < m:
			m = d[j]
			j_min = j
	return j_min

def dijkstra(neigh, edges, k): # uses dijkstra's alg to find distance from 0 vertex to all others
	dist = [0]*len(neigh)
	visited = []
	unvisited = neigh.keys()
	for j in neigh.keys():
		if j == k :
			dist[j] = 0
		else:
			dist[j] = 'inf'
		
	while len(unvisited) > 0:
		u = find_min(unvisited, dist)
		#print unvisited,u, dist[u]
		for v in neigh[u]:
			if dist[u] == 'inf' or edges[(u,v)] == 'inf':
				temp = 'inf'
			else:
				temp = edges[(u,v)] + dist[u]
			if temp < dist[v]:
				dist[v] = temp
			else:
				pass
		unvisited.remove(u)
	return dist

s = 'rosalind_cte.txt'
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
				d = dijkstra(neigh,edges, start)
				if d[end] < 'inf':
					print d[end] + edge_weight,
				else:
					print -1,
				#print
				#print edges
			neigh = {}
			edges = {}	
			new_graph= 'yes'
			n,m = temp.split()
			n = int(n)
			#print 'n is', n
			
			for i in range(0, n):
				neigh.update({i:[]})
			ctr +=1
			
		
		else:
			
			#print 'neigh', len(neigh)
			ctr +=1
			a,b, w = [int(x) for x in line.split()]
			
	                #neigh[b-1].append(a-1)
			
			if new_graph == 'yes':
				start = b-1
				end = a-1
				edge_weight = w
			else:
				neigh[a-1].append(b-1)
				edges.update({(a-1, b-1):w}) # this gives us the weight of the edge (a-1, b-1)
						# definitely poor naming, should be 'weights' or something
				
			
			new_graph = 'no'
			
	d = dijkstra(neigh,edges, start)
	if d[end] < 'inf':
		print d[end] + edge_weight,
	else:
		print -1,
	#print edges
