#Given: A simple graph with n<=1000 vertices in the edge list format.

#Return: The number of connected components in the graph.

import numpy as np
import sys
sys.setrecursionlimit(10000)



def union(A,B):
	C = set()
	for y in A:
		C.add(y)
	#print_set(A)
	#print_set(B)
	#print 'hello'
	for x in B:
		#print x
		#print A
		if x in A:
			##print 'b'
			pass
		else:
			C.add(x)
	return C
		
		
def difference(A,B):
	C = set()
	for y in A:
		C.add(y)
	for x in B:
		if x in A:
			C.remove(x)
	#print 'a;lksdfj'
	return C		
		
		
def intersection(A,B):
	#print 'hello'
	C = set()
	for y in A:
		C.add(y)
	#print A
	#print B
	for x in A:
		if x in B:
			pass
		else:
			#print x
			C.remove(x)
	
	return C
		
		
		
		
comp_dict = {}

comp_ctr = 0

def make_comp(neigh):
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
	return comp_dict

def neighbors(C, neigh):
	D = set()
	for c in C:
		D = union(D, neigh[c])
		
        return D
		
def is_bipartite(neigh): # reads in a dictionary of vertices:neighbors, returns 1 if graph is bipartite and -1 otherwise
		
	
	A = set()
	B = set()
	S = set(neigh.keys())
	#print 'S is initially', S
	v = S.pop()
	#print 'First v is ', v
	A.add(v)
	new_A = set()
	new_B = set()
	new_A.add(v)
	
	while len(S) > 0:
		
		if len(new_A) == 0 and len(new_B) == 0:
			v = S.pop()
			new_A.add(v)
			
		#new_B = difference(neighbors(new_A, neigh), B)
		#new_A = difference(neighbors(new_B, neigh), A)
		#A = union(A, new_A)
		#B = union(B, new_B)
		#S = difference(S, new_A)
		#S = difference(S, new_B)
		
		new_B = neighbors(new_A, neigh).difference(B)
		new_A = neighbors(new_B, neigh).difference(A)
		A = A.union(new_A)
		B = B.union(new_B)
		S = S.difference(new_A)
		S = S.difference(new_B)
		
		
	for a in A:
		if len(set(neigh[a]).intersection(A) ) > 0 :
			#print neigh[a], A
			return -1
			
	
	for b in B:
		if len(set(neigh[b]).intersection(B) ) > 0 :
			#print neigh[b], B
			return -1
	
	#print A
	#print B
	return 1
		
	
def explore(v, neigh, visited, precursor, color):
	#print visited
	#print precursor
	#print neigh[v]
	
	if len(neigh[v]) == 0:
		return visited, color
	
	for u in neigh[v]:
		#print u
		#print visited
		if u not in visited:
			#print 'hello'	
			
			visited.append(u)
			color.append({u: (color[v] + 1) % 1})
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
		
def new_is_bipartite(neigh):
	V, C = explore(i, neigh, [i], [])
	for v in C.keys():
		for u in neigh[v]:
			if C[u] == C[v]:
				return -1
	else:
		return 1
	
		
filename = 'rosalind_bip.txt'


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
				print is_bipartite(neigh),# 'hi'
				
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


	print is_bipartite(neigh)


#for a in neigh.keys():
	#print a, neigh[a]

	

