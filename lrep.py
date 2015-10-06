
import sys


def compute_descendants(v):  # input is a vertex v in a tree
			# output is the number of descendants of v in the tree
	total = 0
	if v not in children and v not in already_done:
		descendants.update({v:0})
		already_done.add(v)
		return 0
	for u in children[v]:
		if u not in children:
			total += 1
		else:
			
			if u in already_done:
				total += descendants[u]
			else:
				descendants.update({u:compute_descendants(u)})
				already_done.add(u)
				total += descendants[u]
	
	
	descendants[v] = total
	return descendants[v]
		

def path_length(v): #input is a vertex v
			#output is the weight of the path from v to the is_root
			
	total = 0
	u = v
	while u in parent:
		total += weight[u]
		u = parent[u]
	return total
	
def string_to(v): #input is a vertex v
			#output is the string corresponding to the path to v
	u = v
	path = []
	length = []
	#print 'checkA'
	while u in parent:
	#	print location[u], 'loc'
	#	print weight[u], 'we'
		path.append(location[u])
		length.append(weight[u])
		u = parent[u]
	#print path
	#print length
	#print 'checkB'
	
	return [path, length]

	
filename = 'rosalind_lrep.txt'
with open(filename,'r') as in_file:
	#trash = in_file.readline()
	temp = in_file.readline()
	s = temp.strip()
	temp = in_file.readline()
	k = temp.strip()
	k = int(k)
	
	children = {}
	parent = {}
	weight = {}
	location = {}
	descendants = {}
	height = {}
	
	is_root = 'yes'
	for line in in_file:
		temp = line.strip()
		[a,b, l, w] = temp.split()
		#if is_root == 'yes': a = 'root'
		w = int(w)
		l = int(l)
		#print 'w =',w, 'l =', l
		parent.update({b:a})
		weight.update({b:w})
		location.update({b:l-1}) # subtract one to change from one based indexing 
				# as given in file
		if a in children:
			children[a].append(b)
		else:
			children.update({a:[b]})
		
		if is_root == 'yes':  height.update({a:0})
		height.update({b: height[a] + 1})
		is_root = 'no'




#for v in weight:
	#print 'weight of', v, ' is ', weight[v]



already_done = set()


for v in children:
	compute_descendants(v)
#compute_descendants('root')



#candidates = set()
max_path_length = 0
winner = 'nobody'




for v in descendants:
	#print descendants[v]
	if descendants[v] >=k:
	#	print v, 'has at least k children'
	#	print ' and path length is ', path_length(v)
		
		#candidates.add(v)
		if path_length(v) > max_path_length:
			max_path_length = path_length(v)
			winner = v

print k
print winner, max_path_length
print 'yes'
[X, Y] = string_to(winner)
#print X
#print Y

answer = ''
for j in range(0, len(X)):
	#print 'help'
	k = -1-j
	#print X[k], Y[k]
	answer += s[X[k]:X[k]+Y[k]]

print answer

#----------------------------------------------------------------#
#----------------------------------------------------------------#	
#----------------------------------------------------------------#

	
#max_height = 0
#for v in height:
	#print v, height[v]
	#if height[v] > max_height:
		#max_height = height[v]


#inv_height = {}


#for v in height:
	#if v in children:
		#pass
	#else:
		#while v != 'node1':
			#inv_height.update({v:
		#if height[v] == max_height - j:
			#total = 0
			#if j == 0: descendants[v] = 0
			#else:
				#print v,  height[v], j
				#for u in children[v]:
					#total += descendants[u]
				#descendants[v] = total





#weight.update({'node1':0})


	


		
#print children['node14']

		
