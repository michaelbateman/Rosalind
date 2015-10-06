
filename = 'rosalind_trie.txt'

L = []

with open(filename, 'r') as input_file:
	for line in input_file:
		L.append(line.strip())
#		print line.strip()
#		print
#		print
#L = sorted(L)

#print L
dict = {} # has the form (letter number, letter): vertex number
ctr = 2 # used to number vertices.  the root is labelled 1
vertex_dict = {}
edge_list = []

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
				print 1, ctr, w[:j][-1]
			else:
				edge_list.append((vertex_dict[w[:j-1]], ctr))
				print vertex_dict[w[:j-1]], ctr, w[:j][-1]
			ctr +=1
			new_path = 1


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
	

				

