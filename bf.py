#Given: a graph with possibly negative edge weights

#Return: The distance between the 0 vertex and all other vertices

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

def dijkstra(neigh, edges): # uses dijkstra's alg to find distance from 0 vertex to all others
	dist = [0]*len(neigh)
	visited = []
	unvisited = neigh.keys()
	for j in neigh.keys():
		if j ==0:
			dist[j] = 0
		else:
			dist[j] = 'inf'
		
	while len(unvisited) > 0:
		u = find_min(unvisited, dist)
		#print unvisited,u, dist[u]
		for v in neigh[u]:
			if dist[u] == 'inf':
				temp = 'inf'
			else:
				temp = edges[(u,v)] + dist[u]
			if temp < dist[v]:
				dist[v] = temp
			else:
				pass
		unvisited.remove(u)
	return dist
			
			
			
			
def bf(neigh,edges):
	dist = [0]*len(neigh)
	visited = []
	unvisited = neigh.keys()
	for j in neigh.keys():
		if j ==0:
			dist[j] = 0
		else:
			dist[j] = 'inf'
						
	for i in range(0, len(neigh)):
		for (u,v) in edges:
			if dist[u] == 'inf':
				temp = 'inf'
			else:
				temp = edges[(u,v)] + dist[u]
			if temp < dist[v]:
				dist[v] = temp
			else:
				pass
			
	return dist
			

s = 'rosalind_bf.txt'
neigh = {}
edges = {}
with open(s, 'r') as input_file:

	n,m = [int(x) for x in input_file.readline().split()]
	deg = [0] * n
	for i in range(0, n):
		neigh.update({i:[]})
	
	for line in input_file:
		a,b,w= [int(x) for x in line.split()]
		neigh[a-1].append(b-1)
		#neigh[b-1].append(a-1)
		edges.update({(a-1, b-1):w}) # this gives us the weight of the edge (a-1, b-1)
						# definitely poor naming, should be 'weights' or something
		
d = dijkstra(neigh,edges)
for j in neigh.keys():
	if d[j] < 'inf':
		print d[j],
	else:
		print 'x',