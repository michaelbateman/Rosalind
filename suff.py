
filename = 'rosalind_trie.txt'

L = []

with open(filename, 'r') as input_file:
	temp = input_file.readline()
	s = temp.strip()
	
len_s = len(s)
for j in range(0, len(s)):
	L.append( s[j:] )

#print L
dict = {} # has the form (letter number, letter): vertex number
ctr = 2 # used to number vertices.  the root is labelled 1
vertex_dict = {}
edge_list = []
children = {}
parent = {}
edge_label = {}

for w in L:
	new_path = 0
	for j in range(1, len(w)+1):
		#print w[:j]
		if w[:j] in vertex_dict:
			pass
		else: 
			
			vertex_dict.update({w[:j]:ctr})
			
			if j == 1 :
				edge_list.append((1,ctr))
				children.update({1:ctr})
				parent.update({ctr:1})
				print 1, ctr, w[:j][-1]
			else:
				edge_list.append((vertex_dict[w[:j-1]], ctr))
				children.update({vertex_dict[w[:j-1]]: ctr})
				parent.update({ctr : vertex_dict[w[:j-1]])
				edge_label.update({  (vertex_dict[w[:j-1]], ctr) : w[j]})
				print vertex_dict[w[:j-1]], ctr, w[:j][-1]
			ctr +=1
			new_path = 1


for v in vertex_dict:
	if len(children[vertex_dict[v]) == 1:
		
		edge_label.update({ (parent[v], 


def label_edge(a,b,y): # input is two vertices a,b together with a word y 
			# which will be the label for the edge (a,b)
			
	edge_label.update({(a,b): y})
	return 0

def remove_child(parent, child):  # input is a vertex parent and a vertex child
				# child is removed from list of children of parent
		
	children[parent].remove(child)
	return 0
	
	
def add_child(parent, child)  # child is added to the list of children of parent

	children[parent].add(child)
	return 0
	

def add_word(w): # adds the word w to a suffix tree already in existence
	j = len(w)
	while w[0:j] not in vertex_dict:
		j-=1
	
	
	for u in children(w[







#filename = 'temp_output.txt'
#with open('a.txt', 'w') as out_file:
	#for w in L:
		##print 'hi'
		##out_file.write('aaa')
		#new_path = 0
		#for j in range(0, len(w)):
			#if (j, w[j]) in dict.keys() and new_path == 0:
				#pass
			#else: 
				#dict.update({(j,w[j]): ctr})
				#if j == 0 :
					##out_file.write('aaa')
					#out_file.write( str(1) + ' ' + str(ctr) + ' ' +  w[j]+ '\n' )
				#else:
					#out_file.write( str( dict[(j-1, w[j-1])]) + ' ' +  str(ctr) + ' ' +  w[j]+ '\n' )
				#ctr +=1
				#new_path = 1
	

				

