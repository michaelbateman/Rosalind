
import sys

	
def find_subseq(s, sub): # input is a string s, and a subsequence subsequence
			# output is a string of indices corresponding to sub
	ans = []	
	j = 0 
	i = 0
	M = len(sub)
	while( i < M ) :
		while( s[j] != sub[i]):
			j+=1
		ans.append(j)
		j+=1
		i+=1
	
	return ans
	

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



filename = 'rosalind_scsp.txt'
with open(filename,'r') as in_file:
	#trash = in_file.readline()
	temp = in_file.readline()
	s = temp.strip()
	
	#trash = in_file.readline()
	temp = in_file.readline()
	t = temp.strip()
	

#print longest_common_subseq(my_dict[1],my_dict[2])


#print len(s) + len(t) - LCIS(my_dict[1],my_dict[2])

subsequence = LCIS(s,t)

s_indices = find_subseq(s, subsequence)
t_indices = find_subseq(t, subsequence)

i = 0
j = 0
L = len(s)
M = len(t)

superstring = ''

while( i < L or j < M ):
	if i not in s_indices and i < L:
		superstring += s[i]
		i += 1
	elif j not in t_indices and j < M:
		superstring += t[j]
		j += 1
	else:
		superstring += s[i]
		i += 1
		j += 1


#print find_subseq('abcdefghij', 'aij')
print superstring