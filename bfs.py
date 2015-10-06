





import numpy as np

s = 'rosalind_bfs.txt'

neigh = {}


def friends(neigh, L):
	T = []
	for x in L:
		for y in neigh[x]:
			T.append(y)	
	#print T	
	return set(T)

def next_sphere(neigh, S): #sphere centered at first vertex (index 0) of radius r
	temp = friends(neigh, [0])
	for j in range(2, r+1):
		new_temp = friends(neigh, temp)
		temp = new_temp
	#print ' sphere radius', r, ' = ', temp		
	return temp
	

def BFS(i, neigh):
	spheres = {}
	spheres.update({1:friends(neigh, [0]) } )
	if i in spheres[1]:	return 1
	for r in range(2, n):
		spheres.update({r:friends(neigh, spheres[r-1]) } ) 
		if i in spheres[r]:
			return r
	return -1
		
		


with open(s, 'r') as input_file:
	n,m = [int(x) for x in input_file.readline().split()]
	for i in range(0, n):
		neigh.update({i:[]})
	for line in input_file:
		a,b = [int(x) for x in line.split()]
		neigh[a-1].append(b-1)

#for i in range(0, n):
	#print neigh[i]




print 0,
for i in range(1, n):
	print BFS(i, neigh), 
	