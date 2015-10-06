#Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.


import numpy as np
import sys
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
		#print len(tree)
	#	print m, len(tree)
		if tree[m:m+2] in ['aa', 'Aa', 'AA']:
		#	print m, len(tree)
			tree = tree[:m] + str(i) + tree[m:]
			m+= 1 + len(str(i))
			i +=1
		#	print m, len(tree)
		else:
			m+=1
		
	
	my_list = tree.replace(',', ' ').replace('(', ' ').replace(')', ' ').replace(';', ' ')
	my_list = my_list.split()
	my_list.sort()
	return my_list, tree



#def combine(dict1 = {'dom': a, 'het':b, 'rec':c}, dict2 = {'dom': d, 'het':e, 'rec':f} ):  # input is two three-tuples corresponding to D,H, R probs for two children
			# out put is the three-tuple corresponding to D.H.R prob for parent
def combine(dict1, dict2):	
	temp = 0
	for type1 in dict1:
		for type2 in dict2:
			weight =  dict1[type1] * dict2[type2]
			temp +=  np.multiply( weight, my_dict[type1+type2] ) 
			
	[x,y,z] = temp
	return {'dom': x, 'het': y, 'rec': z}


def find_prob(v): # input is a tree, output is a dictionary corresponding to D,H,R probs for the path_to_root
	#print children[v], ' is children of', v
	if len(children[v]) == 2:
		(a,b) = children[v]
	else :
		if  v[-2:] == 'AA':
			return {'dom': 1, 'het': 0, 'rec': 0}
		elif  v[-2:] == 'Aa':
			return {'dom': 0, 'het': 1, 'rec': 0}
		elif  v[-2:] == 'aa':
			return {'dom': 0, 'het': 0, 'rec': 1}
		else:
			print  v
			print 'problem!!!'
	return combine(find_prob(a), find_prob(b))


		
		
# my_dict gives prob of (dom, het, rec) given parents domdom, domhet, etc.
my_dict = {  'domdom': (1,0,0), 'domhet' : (.5, .5, 0), 'domrec': (0,1,0), 
	     'hetdom': (.5, .5, 0), 'hethet' : (.25, .5, .25), 'hetrec': (0, .5, .5),
	     'recdom': (0, 1,0), 'rechet' : (0, .5, .5), 'recrec': (0, 0, 1)  }



filename = 'rosalind_mend.txt'
#print 'heifhae'
with open(filename, 'r') as input_file:
	temp = input_file.readline();
	tree = temp.strip()
	#print 'ok'
	my_list, tree = listify(tree)
	#print 'now'
#print my_list
#print tree
path_dict = {}

#for x in my_list:  
	#path_dict.update({x:path_to_root(x, tree)})
	
#print 'hello'

children = {}
for x in my_list:
	P = path_to_root(x, tree)
	#print P
	for j in range(0, len(P)):
		if P[j] in children.keys():
			pass
		else:
			temp = set()
			children.update({P[j]:temp})
		if j > 0: 
			children[P[j]].add(P[j-1])
			#print 'my path is', P
			#print 'my new child is', P
			
	root = P[-1]
#print 'hello again'
#print children	
ans =  find_prob(P[-1])
print ans['dom'], ans['het'], ans['rec']
