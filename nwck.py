#Given: A collection of n trees (n<=40) in Newick format, with each tree containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.

#Return: A collection of n positive integers, for which the kth integer represents the distance between xk and yk in Tk.


import numpy as np
import string
#import re


#def dist(a,b, T): # computes distance between vertices a and b in a tree given in newick format
	
	
neigh = {}


def friends(neigh, L):
	T = []
	for x in L:
		for y in neigh[x]:
			T.append(y)	
	#print T	
	return set(T)

#def next_sphere(neigh, S): #sphere centered at first vertex (index 0) of radius r
	#temp = friends(neigh, [0])
	#for j in range(2, r+1):
		#new_temp = friends(neigh, temp)
		#temp = new_temp
	##print ' sphere radius', r, ' = ', temp		
	#return temp
	

def dist(u,v, neigh):
	spheres = {}
	spheres.update({1:friends(neigh, [u]) } )
	if v in spheres[1]:	return 1
	for r in range(2, n):
		spheres.update({r:friends(neigh, spheres[r-1]) } ) 
		if v in spheres[r]:
			return r
	return -1
		
		



def print_edges(s, v): # s is a list of vertices inside the parens, all vertices should be named; v is the parent of all vertices listed in s
	L = s.split(',')
	for x in L:
		print v, x

	
def make_edge_list(newick): # input is a tree in newick format, output is an array containing the rows of an edge/list file for the tree
	s = newick
	ctr = 0
	while len(s) > 0:
		#print s
		for j in range(0, len(s)):
			if s[j] == '(':
				start = j
				#print 'start = ', start
			elif s[j] == ')':
				end = j
				#print 'end = ', end
				if s[j+1] == ',' or s[j+1] == ')':
					
					print_edges(s[start+1:end], ctr)
					s = s[:start] + str(ctr) + s[end+1]
					ctr +=1
					
				else:
					
					i = end +1
					while s[i] != ',' and s[i] != ')' and s[i] != ';':
						#print i, end +1
						#print s[end +1: i+1]
						node = s[end +1: i+1]
						#print node
						i+=1
					print_edges(s[start+1:end], node)
					s = s[:start] +  s[end+1:]
				break
			elif s[j] == ';':
				s = ''
				break
				#pass
					

def distance(u,v, newick):
	OK = 0
	if newick.find('('+u +')') > 0:
		OK = 1
	elif newick.find(','+u + ')') > 0:
		OK = 1
	elif newick.find('('+u +',') > 0:
		OK = 1
	elif newick.find(','+u + ',') > 0:
		OK = 1
		
	if OK ==1:
		print
	else: print 'oops'
	

#def convert(tree): # input tree in newick format, output ...

def find_parent(x,tree): # returns the parent of x in tree, where tree is in newick format
			# format of parent is (.....) without the identifying name that could trail the (...)
	j = string.find(tree,x)
	if j==0:# or j+len(x)-1 == len(tree):
		return x
	#print j, x, tree, j+len(x) - 1
	
		
		
	k = j+len(x)-1
	ctr = 0
	while ctr < 1:
		k+=1
		if tree[k] == ')':
			ctr +=1
		elif tree[k] == '(':
			ctr -=1
		elif tree[k] == ';':
			return x
		
	i = j
	ctr = 0
	while ctr <1:
		i-=  1
		#print i
		if tree[i] == '(':
			ctr +=1
		elif tree[i] == ')':
			ctr -=1
		
	return tree[i:k+1]

def find_subtree(x,tree):
	j = string.find(tree,x)
	#if j==0:# or j+len(x)-1 == len(tree):
		#return x
	#print j, x, tree, j+len(x) - 1
	
	
	if tree[j-1] != ')':
		return x
	
	
	i = j-1
	ctr = 1
	while ctr > 0:
		i-=  1
		#print i
		if tree[i] == '(':
			ctr -=1
		elif tree[i] == ')':
			ctr +=1
		
	
	return tree[i:j]



def path_to_root(x, tree): # input a node x and a tree in newick format, return the path from x to the path_to_root
	#print x
	x = find_subtree(x,tree)
	path = [x]
	y = x
	temp = find_parent(y, tree)
	while temp != y:
		path.append(temp)
		y = temp
		temp = find_parent(y, tree)
		#print y,x
		
	return path
		
	



filename = 'rosalind_nwck.txt'

with open(filename, 'r') as input_file:
	for line in input_file:
		if len(line.strip()) == 0:
			pass
		elif line.strip()[-1] == ';':
			
			newick = line.strip()
			#newick = newick.strip(';')
			#tree = convert(newick)
			#tree = make_edge_list(newick)
		elif len(line.strip()) > 0:			
			temp = line.strip()
			u, v = temp.split()
			
			P = path_to_root(u, newick)
			Q = path_to_root(v, newick)
			#print P
			#print Q
			#print len(P), len(Q),
			
			i = 0 
			#if len(P)<2:
				#dist = len(Q) - 1
			#elif len(Q)<2:
				#dist = len(P) - 1
			if set(P).issubset(set(Q)):
				dist = len(Q) - len(P)
			elif set(Q).issubset(set(P)):
				dist = len(P) - len(Q)
			else:
				while P[-2 - i] == Q[-2 - i]: # start w/ -2 b/c P[-1] = Q[-1] is always root
					i+=1
				dist = (len(P)-1) + (len(Q) - 1) - 2*i
			print dist,
			#print i, dist
			#print
			#print dist(a,b, tree)
		





#s = 'temp_output.txt'
#
#with open(s, 'r') as input_file:
	#n,m = [int(x) for x in input_file.readline().split()]
	#for i in range(0, n):
		#neigh.update({i:[]})
	#for line in input_file:
		#a,b = [int(x) for x in line.split()]
		#neigh[a-1].append(b-1)
		#neigh[b-1].append(a-1)
	
#print dist(u,v,neigh)