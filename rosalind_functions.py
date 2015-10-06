import sys
import scipy.misc
import numpy as np
import time
import re

genetic_code = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}



		


def make_dict(s):
    try:
        input_file = open(s, "r")
        #print "input file is", input_file.name
    except IOError:
        print "Oh no, we couldn't open our file!"

    dict = {}
    for line in input_file:
	temp = line.split()
	dict.update(  {temp[0]:float(temp[1])}  )
	
    return dict	
    

def occurences(s,w):	# nice code stolen from http://stackoverflow.com/questions/2970520/string-count-with-overlapping-occurrences
			# from problem 1a
	ctr = 0
	start = 0
	
	while True:
		start = s.find(w,start) + 1
		if start > 0:
			ctr +=1
		else:
			return ctr	

def make_kmers(k):
	kmers = ['']
	bases = ['A', 'C', 'G', 'T']
	j =0 
	for i in range(0, k):
		new = []
		for w in kmers:
			for b in bases:
				new.append(w + b)
				#print w+b, k
						
		kmers = new
	
	return kmers
	

def read_string(filename): # input is name of a file containing a string, output is that string
	with open(filename, 'r') as in_file:
		temp = in_file.readline()
		temp = temp.strip()
	return temp

def read_two_strings(filename): # input is name of a file containing two string, output is those strings
	with open(filename, 'r') as in_file:
		temp = in_file.readline()
		temp = temp.strip()
		
		temp2 = in_file.readline()
		temp2 = temp2.strip()
		
	return temp, temp2



def rev_comp(dna): #input is a string, output is reverse complement of that string
			# from problem 1b
	rev_comp = ''

	comp = { 'A': 'T', 'T':'A', 'C':'G', 'G':'C'}

	L = len(dna)
	i = 1

	while i <= L:
		rev_comp = rev_comp + comp[dna[-i]]
		i +=1
	
	return rev_comp

#def find_occurrences(sub, s): # returns locations of sub inside a string s, using 0-based indexing
	#L = len(s)
	#M = len(sub)
	#ans = []
	#for j in range(0, L - M + 1):
		#if s[j:j+M] == sub:
			#ans.append(j)
		#else:
			#pass
	
	#return ans
		
	
def find_occurrences(sub, s):
	temp = '(?=' + sub + ')'
	#print [m.start() for m in re.finditer(temp, s)]
	return [m.start() for m in re.finditer(temp, s)]
	
	
def is_clump(L,t, kmer, my_string):
	#print kmer
	start = time.clock()
	my_list = find_occurrences(kmer, my_string)
	end = time.clock()
	time_A = end - start
	M = len(my_list)
	start = time.clock()
	for j in range(t - 1, M):
		if len(kmer) + my_list[j] - my_list[j-t + 1] <= L : 
			return 'yes'
	end = time.clock()
	time_B = end - start	
	#print float(time_A), float(time_B)
	return 'no'
	
def find_clumps(L,t, my_string, my_list): #finds all words in my_list forming (L,t) clumps inside my_string
	#kmers = make_kmers(k)
	#length = len(kmers)
	#print 'done making kmers'
	ans = []
	ind = 0
	#print my_list
	for w in my_list:
		ind +=1
		#print ind
		if ind % 10000 ==0 : print ind, length, float(ind) / float(length)
		if is_clump(L,t, w, my_string) == 'yes':
			ans.append(w)
	#		print 'ehhlo', ans
			
		else:
			pass
	#print 'ans is', ans
		
	return ans
		

def neighbors(t): # input is a string t, output is the set of strings at hamming distance 1 from t
	bases = ['A', 'C', 'G', 'T']
	L = len(t)
	ans = []
	for j in range(0, L):
		for b in bases:
			ans.append( t[:j] + b + t[j+1:] )
	
	return set(ans)
	
	   
def neighborhood(S): 
	temp = set()
	
	
	for s in S:
		temp.update(neighbors(s))
	
	return temp

def ball(S,k): # input is a set of strings, output is the set of strings that are distance at most k from an elt of S
	#temp  = set()
	for j in range(0, k):
		S = neighborhood(S)
	#print 'neighborhood is ', neighborhood(S)
#		print S
	return S


def rna2prot(rna):  #turns a string rna into a string of amino acids
	L = len(rna)
	prot = ''
	for j in range(0, L):
		if j%3 == 0:
			if genetic_code[rna[j:j+3]] == 'Stop': return prot
			else: prot = prot + genetic_code[rna[j:j+3]]
		else:
			pass
	return prot

def dna2rna(dna): # changes all T's into U's
	L = len(dna)
	rna = ''
	for j in range(0,L):
		if dna[j] == 'T':
			rna = rna + 'U'
		else:
			rna = rna +  dna[j]
	return rna

def dna2prot(dna):  #turns a string rna into a string of amino acids
	rna = dna2rna(dna)
	return rna2prot(rna)


def total_mass(prot):
	N = len(prot)
	total =  0
	for j in range(0, N):
		total += mass_dict[prot[j]]
	return total


def read_fasta(file_name):
	
	s = file_name

	try:
    		input_file = open(s, "r")
    	#	print "input file is", input_file.name
	except IOError:
	    	print "Oh no, we couldn't open our file!"
	

	sample_dict = {}
	temp = ''
	sample = ''
	ctr = -1 
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
		A[i][0] = i
		S[i][0] = S[i-1][0] + s[i-1]
		T[i][0] = T[i-1][0] + '-'
	for j in range(1, N+1):
		A[0][j] = j
		S[0][j] = S[0][j-1] + '-'
		T[0][j] = T[0][j-1] + t[j-1]
	for i in range(1, M+1):
		for j in range(1, N+1):
			# notice the indexing for A,S,T is one off from that of s,t
			a = A[i-1][j] + 1
			x = S[i-1][j] + s[i-1]
			X = T[i-1][j] + '-'
			
			b = A[i][j-1] + 1
			y = S[i][j-1] + '-'
			Y = T[i][j-1] + t[j-1]
			
			if s[i-1] == t[j-1]:
				c = A[i-1][j-1]
				
			else:
				c = A[i-1][j-1] + 1
			
			#print i, j, T[i-1][j-1] , t[j-1]
			z = S[i-1][j-1] +  s[i-1]
			Z = T[i-1][j-1] +  t[j-1]
			
			A[i][j] = min(a,b,c)
			if a == min(a,b,c):
				S[i][j] = x
				T[i][j] = X
			elif b == min(a,b,c):
				S[i][j] = y
				T[i][j] = Y
			else:
				S[i][j] = z
				T[i][j] = Z
	#print A
	return [A[M][N], S[M][N], T[M][N]]

def align(s,t, g, P):# returns global optimal alignment between any substrings of s,t
	# g is a linear gap penalty
	# P (see below) is the scoring matrix, 
	# P is a dictionary, with argument being a pair
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

def num_min_aligns(s,t):
	
	M = len(s)
	N = len(t)
	
	# A[i][j] is edit distance between first i letters of s and first j letters of t
	# S[i][j], T[i][j] are the superstrings realizing this edit distance
	
	# B[i][j] is the number of pairs of superstrings realizing edit distance between
	#    first i letters of s and first j letters of t
	
	A = [[0 for j in range(0, N+1)] for i in range(0, M+1)]
	S = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	T = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	
	B = [[0 for j in range(0, N+1)] for i in range(0, M+1)]
	
	
	# Initialize A and B
	
	B[0][0] = 1
	
	for i in range(1, M+1):
		A[i][0] = i
		S[i][0] = S[i-1][0] + s[i-1]
		T[i][0] = T[i-1][0] + '-'
		
		B[i][0] = 1
		
	for j in range(1, N+1):
		A[0][j] = j
		S[0][j] = S[0][j-1] + '-'
		T[0][j] = T[0][j-1] + t[j-1]
		
		B[0][j] = 1
		
	for i in range(1, M+1):
		for j in range(1, N+1):
			# notice the indexing for A,S,T is one off from that of s,t
			a = A[i-1][j] + 1
			x = S[i-1][j] + s[i-1]
			X = T[i-1][j] + '-'
			
			b = A[i][j-1] + 1
			y = S[i][j-1] + '-'
			Y = T[i][j-1] + t[j-1]
			
			if s[i-1] == t[j-1]:
				c = A[i-1][j-1]
				
			else:
				c = A[i-1][j-1] + 1
			
			#print i, j, T[i-1][j-1] , t[j-1]
			z = S[i-1][j-1] +  s[i-1]
			Z = T[i-1][j-1] +  t[j-1]
			
			A[i][j] = min(a,b,c)
			if a == min(a,b,c):
				S[i][j] = x
				T[i][j] = X
			elif b == min(a,b,c):
				S[i][j] = y
				T[i][j] = Y
			else:
				S[i][j] = z
				T[i][j] = Z
				
			# This loop, up to here, is copied directly from the fcn edit_distance
			# starting here we define the matrix B
			
			
			B[i][j] = 0
			
			if a == min(a,b,c):  B[i][j] += B[i-1][j]
			
			if b == min(a,b,c):  B[i][j] += B[i][j-1]
				
			if c == min(a,b,c):  B[i][j] += B[i-1][j-1]
			
			B[i][j] = B[i][j] % 134217727
			
			
			
			#print S[i][j]
			#print T[i][j]
			#print B[i][j]
	#print A
	return [A[M][N], S[M][N], T[M][N], B[M][N]]



	
def local_optimal_align(s,t, g, P): # returns optimal local alignment between any substrings of s,t
	# g is a linear gap penalty
	# P (see below) is the scoring matrix, 
	# P is a dictionary, with argument being a pair
	
	M = len(s)
	N = len(t)
	
	# A[i][j] is edit distance between first i letters of s and first j letters of t
	# A is the matrix keeping track of alignments that are still running at i,j
	# X is the matrix keeping track of 
	# A_S[i][j], A_T[i][j]  and X_S[i][j], X_T[i][j] are the superstrings realizing 
	#	these maximal alignment scores
	
	A = [[0 for j in range(0, N+1)] for i in range(0, M+1)]
	A_S = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	A_T = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	
	
	
	#X = [[0 for j in range(0, N+1)] for i in range(0, M+1)]
	#X_S = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	#X_T = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	
	max_score = 0 
	max_S = ''
	max_T = ''
	
	# Initialize A and B
	
	for i in range(1, M+1):
		A[i][0] = -i * g
		A_S[i][0] = A_S[i-1][0] + s[i-1]
		A_T[i][0] = A_T[i-1][0] + '-'
	for j in range(1, N+1):
		A[0][j] = - j * g
		A_S[0][j] = A_S[0][j-1] + '-'
		A_T[0][j] = A_T[0][j-1] + t[j-1]
	for i in range(1, M+1):
		for j in range(1, N+1):
			# notice the indexing for A,S,T is one off from that of s,t
			a =  A[i-1][j] - g
			x = A_S[i-1][j] + s[i-1]
			X = A_T[i-1][j] + '-'
			
			b = A[i][j-1] - g
			y = A_S[i][j-1] + '-'
			Y = A_T[i][j-1] + t[j-1]
			
			c = A[i-1][j-1] + P[(s[i-1], t[j-1])]
			
			#print i, j, T[i-1][j-1] , t[j-1]
			z = A_S[i-1][j-1] +  s[i-1]
			Z = A_T[i-1][j-1] +  t[j-1]
			
			#temp1 = - g
			fresh_start = P[(s[i-1], t[j-1])]
			
			
			A[i][j] = max(a,b,c, fresh_start)
			if a == max(a,b,c, fresh_start):
				A_S[i][j] = x
				A_T[i][j] = X
			elif b == max(a,b,c, fresh_start):
				A_S[i][j] = y
				A_T[i][j] = Y
			elif c == max(a,b,c, fresh_start):
				A_S[i][j] = z
				A_T[i][j] = Z
			else:  # if fresh_start is the minimum
				A_S[i][j] = s[i-1]
				A_T[i][j] = t[j-1]
				
			#X[i][j] = max(X[i-1][j], X[i][j-1], X[i-1][j-1], A[i][j])
			
			#if   X[i-1][j] == max(X[i-1][j], X[i][j-1], X[i-1][j-1], A[i][j]):
				#X_S
			
			if A[i][j] > max_score:
				max_score = A[i][j]
				max_S = A_S[i][j]
				max_T = A_T[i][j]
			else:
				pass
			#print max_score, ' 000  ', max_S, '  222   ', max_T
				
	#print A
	return [max_score, max_S, max_T]
	#return [A, A_S, A_T]

def compress(s): # input is a string s, possibly with some gaps
		# output is s without any gaps
		
	L = len(s)
	j = 0
	while j < len(s):
		if s[j] == '-':
			s = s[:j] + s[j+1:]
		else:
			j+=1

	return s


def semiglobal_align(s,t, g, P):# returns semiglobal optimal alignment between any substrings of s,t
	# this means gaps are allowed on the ends of the alignments for free
	# This is realized by changing the initial conditions on the matrix A to allow for
	# 	free gaps on the left, and by keeping track of a score matrix G to allow for 
	#	free gaps on the right
	
	
	# g is a linear gap penalty
	# P (see below) is the scoring matrix, 
	# P is a dictionary, with argument being a pair
	M = len(s)
	N = len(t)
	
	# A[i][j] is edit distance between first i letters of s and first j letters of t
	# S[i][j], T[i][j] are the superstrings realizing this edit distance
	
	A = [[0 for j in range(0, N+1)] for i in range(0, M+1)]
	G = [[0 for j in range(0, N+1)] for i in range(0, M+1)]
	
	S = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	T = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	
	G_S = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	G_T = [['' for j in range(0, N+1)] for i in range(0, M+1)]
	
	# Initialize A and B
	
	for i in range(1, M+1):
		A[i][0] = 0 # because gaps are free on the end  # -i * g
		G[i][0] = 0 # because gaps are free on the end  # -i * g
		S[i][0] = S[i-1][0] + s[i-1]
		T[i][0] = T[i-1][0] + '-'
	for j in range(1, N+1):
		A[0][j] = 0 # because gaps are free on the end  # - j * g
		G[0][j] = 0 # because gaps are free on the end  # - j * g
		S[0][j] = S[0][j-1] + '-'
		T[0][j] = T[0][j-1] + t[j-1]
	for i in range(1, M+1):
		for j in range(1, N+1):
			# notice the indexing for A,S,T is one off from that of s,t
			a = A[i-1][j] - g
			x = S[i-1][j] + s[i-1]
			X = T[i-1][j] + '-'
			a_end = G[i-1][j] 
			
			
			b = A[i][j-1] - g
			y = S[i][j-1] + '-'
			Y = T[i][j-1] + t[j-1]
			b_end = G[i][j-1]
			#print s[i-1], t[i-1], P[(s[i-1], t[i-1])]
			#print P[(s[i-1], t[i-1])]
			c = A[i-1][j-1] + P[(s[i-1], t[j-1])]
			#print i, j, T[i-1][j-1] , t[j-1]
			z = S[i-1][j-1] +  s[i-1]
			Z = T[i-1][j-1] +  t[j-1]
			
			A[i][j] = max(a,b,c)
			G[i][j] = max(a_end,b_end,c)
			if a == max(a,b,c):
				S[i][j] = x
				T[i][j] = X
			elif b == max(a,b,c):
				S[i][j] = y
				T[i][j] = Y
			else:
				S[i][j] = z
				T[i][j] = Z
				
			if a_end == max(a_end,b_end):
				G_S[i][j] = x
				G_T[i][j] = X
			else:# b_end == max(a_end,b_end):
				G_S[i][j] = y
				G_T[i][j] = Y
			#else:
				#G_S[i][j] = z
				#G_T[i][j] = Z
				
			if A[i][j] > G[i][j]:
				G[i][j] = A[i][j]
				G_S[i][j] = S[i][j]
				G_T[i][j] = T[i][j]
				
				
	if G[M][N] > A[M][N]:
		return [G[M][N], G_S[M][N], G_T[M][N]]
	return [A[M][N], S[M][N], T[M][N]]

def score(s,t, g, P): #returns the edit distance between s, t with matrix P and linear gap penalty g
	L = len(s)
	total = 0
	for j in range(0, L):
		if s[j] == '-' or t[j] == '-':
			total = total - g
		else:
			total = total + P[(s[j], t[j])]
	left_gain = 0	
	if s[0] == '-':
		for j in range(1,L):
			if s[j] != '-':
				left_gain = j
				break
	if t[0] == '-':
		for j in range(1,L):
			if t[j] != '-':
				left_gain = j
				break	
		
	if s[-1] == '-':
		for j in range(2,L+1):
			if s[-j] != '-':
				right_gain = j-1
				break
	if t[-1] == '-':
		for j in range(2,L+1):
			if t[-j] != '-':
				right_gain = j-1
				break	
		
	print right_gain, left_gain, total
	total = total + g * (right_gain + left_gain)
	
	
	return total