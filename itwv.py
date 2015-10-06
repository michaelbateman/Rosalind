
import sys

	
def local_interweave(u,t,w): # input are two patterns u,t, and a longer word w
				# output is 'yes' if u,t can interweave disjointly to form w
		
	#print 'help'
	M = len(u)
	N = len(t)
	
	A = [[ set() for j in range(0, N+1)] for j in range(0, M+1)]
	# A[i][j] is the list of ways that u[0:i] and t[0:j] interleave into w[0: i+j]
	
	
	for i in range(0, M+1):
		#print i
		if u[0:i] == w[0:i]:
			A[i][0].add( u[0:i] )
			#print A[i][0]
	for j in range(0, N+1):
		#print j
		if t[0:j] == w[0:j]:
			A[0][j].add( t[0:j] )
		
	for i in range(1, M+1):
		for j in range(1, N+1):
		#	print i, j
			# notice indexing for x, y is zero based, but indexing for A is one based
			temp1 = set()
			temp2 = set()
			if u[i-1] == w[i+j-1]:
				for x in A[i-1][j]:
					temp1.add(x+u[i-1])
				#temp1 = A[i-1][j].union(set(u[i-1])
			else:
				temp1 = set()
			
			if t[j-1] == w[i+j -1]:
				for x in A[i][j-1]:
					temp2.add(x + t[j-1])
				#temp2 = A[i][j-1].union(set(t[j-1])
			else:
				temp2 = set()
			
			A[i][j] = set.union(temp1, temp2)
			#print A[i][j]
	#print A
	if len(A[M][N]) > 0:
		#print 'yes'
		return 'yes'
	else:
		return 'no'
	
	
	
	
def global_interweave(u,t,s):  # input are two patterns u,t, and a (potentially much) 
				#	longer word s
				# output is 'yes' if u,t can interweave disjointly to 
				#	form a substring of s
	
	L = len(s)
	for k in range(0, L - len(u)- len(t) + 1):
		w = s[k:k+ len(u) + len(t)]
		if local_interweave(u,t,w) == 'yes':
			return 1
		
	return 0
		
	
	
filename = 'rosalind_itwv.txt'
with open(filename,'r') as in_file:
	#trash = in_file.readline()
	temp = in_file.readline()
	s = temp.strip()
	
	sub = []
	
	for line in in_file:
		temp = line.strip()
		sub.append(temp)
		
		
#print sub

for i in range(0,len(sub)):
	for j in range(0, len(sub)):
		print global_interweave(sub[i], sub[j], s),
	print