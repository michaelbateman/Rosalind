#Given: A rooted binary tree T in Newick format encoding an individual's pedigree for a Mendelian factor whose alleles are A (dominant) and a (recessive).

#Return: Three numbers between 0 and 1, corresponding to the respective probabilities that the individual at the root of T will exhibit the "AA", "Aa" and "aa" genotypes.


import sys
import numpy as np
import string

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

def find_subtree(x,tree): # takes in a vertex x from a tree in newick format, returns the string corresponding to the subtree rooted at x
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
		
	
def listify(tree):  #input a tree in newick format, output a list of species in the tree in lex order
	i = 0
	m = 0
	while m < len(tree):
		print len(tree)
		if tree[m:m+2] in ['aa', 'Aa', 'AA']:
			tree.insert(m, i)
			m+=2
		else:
			m+=1
		
	
	my_list = tree.replace(',', ' ').replace('(', ' ').replace(')', ' ').replace(';', ' ')
	my_list = my_list.split()
	my_list.sort()
	return my_list

filename = 'rosalind_ctbl.txt'

with open(filename, 'r') as input_file:
	temp = input_file.readline();
	tree = temp.strip()
	
	#my_list = tree
	#print my_list
	#my_list = my_list.replace(',', ' ').replace('(', ' ').replace(')', ' ').replace(';', ' ')
	#print my_list
	#my_list = my_list.split()
	#my_list.sort()
	my_list = listify(tree)

n = len(my_list)





sys.exit()

#print my_list
#print tree
#print len(my_list)
visited = []
for x in my_list:
	P = path_to_root(x, tree)
	for y in P:
		if y in visited:
			pass
		else:
		#	print y
			visited.append(y)
			L = listify(find_subtree(y, tree))
			if len(L)<=1 or len(L) >= n-1:
			#	if len(L) >= n-1: print 'passing', len(L), n
				pass
			else:
				my_row = ''
				for z in my_list:
					if z in L:
						#print 1,
						my_row+=str(1)
						pass
					else:
						#print 0,
						my_row+=str(0)
						pass
				print my_row
		

#print len(visited), len(my_list)
#for x in my_list:
	#print x

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