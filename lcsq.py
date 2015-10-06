
import sys


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
	

def longest_common_subseq(x,y): # x, y are strings
	if len(x)== 0 or len(y) == 0:
		return ''
	if x[-1] == y[-1]:
		return longest_common_subseq(x[:-1], y[:-1])+x[-1]
	temp1 = longest_common_subseq(x[:-1], y)
	temp2 = longest_common_subseq(x, y[:-1])
	if len(temp1) > len(temp2):
		return temp1
	else:
		return temp2
	
	
def LCIS(x,y): # input is two strings x,y
		# output is the longest common increasing subsequence of x and y
	#print x
	#print y
	M = len(x)
	N = len(y)
	
	A = [[0 for j in range(0, N+1)] for j in range(0, M+1)]
	#A[i][j] is the longest substring in shared by the first i letters of x and the first j letters of y
	
	
	#for L in range(0, max(len(x), len(y))):
		#A[0][L] = ''
		#A[L][0] = ''
		#for i in range(1, L+1):
			#if x[i] == y[L]:
				#A[i][L] = A[i-1][L-1] + x[i]
			#else:
				#if len(A[i][L-1] ) > len(A[i-1][L]):
					#A[i][L] = A[i][L-1]
				#else:
	A[0][1] = 34				#A[i][L] = A[i-1][L]
#	print A
	for i in range(0, M+1):
		#print i
		A[i][0] = ''
	for j in range(0, N+1):
		#print j
		A[0][j] = ''
		
	for i in range(1, M+1):
		for j in range(1, N+1):
		#	print i, j
			# notice indexing for x, y is zero based, but indexing for A is one based
			if x[i-1] == y[j-1]:
				A[i][j] = A[i-1][j-1] + x[i-1]
			else:
				if len(A[i][j-1] ) > len(A[i-1][j]):
					A[i][j] = A[i][j-1]
				else:
					A[i][j] = A[i-1][j]
	return A[M][N]		



filename = 'rosalind_lcsq.txt'
#with open(filename,'r') as in_file:
	#trash = in_file.readline()
	#temp = in_file.readline()
	#s = temp.strip()
	
	#trash = in_file.readline()
	#temp = in_file.readline()
	#t = temp.strip()
	
my_dict = read_fasta(filename)

#print my_dict


#print longest_common_subseq(my_dict[1],my_dict[2])
print LCIS(my_dict[1],my_dict[2])

