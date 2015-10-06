import sys

def read_fasta(filename):
	
	s = filename

	try:
    		input_file = open(s, "r")
    	#	print "input file is", input_file.name
	except IOError:
	    	print "Oh no, we couldn't open our file!"
	

	sample_dict = {}
	temp = ''
	sample = ''
	ctr = 0 
	for line in input_file:
	    if '>' in line:	
		ctr +=1
	#	print ctr
		temp = line.rstrip()
		sample = temp.lstrip('>')
		#print 'SAMPLE:  ', temp2
		my_dna = ''
	    else:
		my_dna = my_dna + line.strip()
		sample_dict.update({ ctr: my_dna })
	#	print my_dna
	
	
	return sample_dict
	

def read_blosum(filename): # reads blosum62 matrix from filename
	
	with open(filename, 'r') as in_file:
		temp = in_file.readline()
		temp = temp.strip()
		index = temp.split()
		
		#A = [[0 for i in range(0, len(index))]  for j in range(0, len(index)) ]
		
		my_dict = {} # make a dictionary A to encode values
		i = 0
		for line in in_file:
			temp = line.strip()
			L = line.split()
			current = L.pop(0)
			j = 0
			for x in index:
				my_dict.update({ ( current, x ): int(L[j]) })
				#A[i][:] = [L[j] for j in range(0, len(L))]
				j+=1
			#i +=1
			
		return my_dict
	
def edit_distance(s,t):
	M = len(s)
	N = len(t)
	
	# A[i][j] is edit distance between first i letters of s and first j letters of t
	# S[i][j], T[i][j] are the superstrings realizing this edit distance
	
	A = [[0 for j in range(0, N+1)] for i in range(0, M+1)]
	S = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	T = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	
	# Initialize A and B
	
	for i in range(1, M+1):
		A[i][0] = -i * g
		S[i][0] = S[i-1][0] + s[i-1]
		T[i][0] = T[i-1][0] + '-'
	for j in range(1, N+1):
		A[0][j] = - j * g
		S[0][j] = S[0][j-1] + '-'
		T[0][j] = T[0][j-1] + t[j-1]
	for i in range(1, M+1):
		for j in range(1, N+1):
			# notice the indexing for A,S,T is one off from that of s,t
			a = A[i-1][j] - g
			x = S[i-1][j] + s[i-1]
			X = T[i-1][j] + '-'
			
			b = A[i][j-1] - g
			y = S[i][j-1] + '-'
			Y = T[i][j-1] + t[j-1]
			#print s[i-1], t[i-1], P[(s[i-1], t[i-1])]
			#print P[(s[i-1], t[i-1])]
			c = A[i-1][j-1] + P[(s[i-1], t[j-1])]
			#print i, j, T[i-1][j-1] , t[j-1]
			z = S[i-1][j-1] +  s[i-1]
			Z = T[i-1][j-1] +  t[j-1]
			
			A[i][j] = max(a,b,c)
			if a == max(a,b,c):
				S[i][j] = x
				T[i][j] = X
			elif b == max(a,b,c):
				S[i][j] = y
				T[i][j] = Y
			else:
				S[i][j] = z
				T[i][j] = Z
	#print A
	return [A[M][N], S[M][N], T[M][N]]

filename = 'rosalind_glob.txt'
g = 5 # gap penalty
P = read_blosum('blosum62.txt')
#print P
#print P[('Y','Y')]


my_dict = read_fasta(filename)
#print my_dict[1]
#print my_dict[2]

[dist, s, t] = edit_distance(my_dict[1],my_dict[2])
print dist
#print s
#print
#print t