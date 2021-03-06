#Given: A positive integer n<=10000 followed by a permutation pi of length n.

#Return: A longest increasing subsequence of pi, followed by a longest decreasing subsequence of pi.


import numpy as np
import sys
sys.setrecursionlimit(10000)


def find(k, A):  # finds k in a sorted array A, returns i s.t. A[i] = k
		# if k is not in A then find returns i st   A[i-1] < k < A[i]
        bot =0
        top = len(A)-1
	if A[bot] == k: return bot
	if A[top] == k: return top
      	if k < A[0]: return 0
	if k > A[len(A)-1]: return len(A)
        while bot < top:
			
                if top == bot + 1:
			return top
                mid = (bot + top)  / 2
		#print bot, mid, top
        #       print ' k = ' , k
        #       print ' A[mid] = ', A[mid]
                if A[mid] == k: return mid 
		elif A[mid]< k: 
			bot = mid
		elif k < A[mid]:
			top = mid 


def extend(X,M, pred, i, L): 
	bot = 1
	top = L
	#print X[i], ' and L =', L
	if X[M[L]] < X[i]:
		new_L = L+1
	else:
		entered_loop = 0
		#find largest j such that X[M[j]] < X[i]
		while X[M[bot]] < X[i] :
			entered_loop = 1
			if bot == top - 1:
				new_L = bot + 1
				break
			mid = (bot + top)  / 2	
			if X[M[mid]] < X[i]: bot = mid
			elif X[M[mid]] >= X[i] :
				top = mid 
			
		if entered_loop == 0: new_L = 1
		else: new_L = bot + 1
		
	
	#print 'new_L = ', new_L
	if new_L > 1:
		pred.append(M[new_L - 1	])
	else:
		pred.append('none')
	
	if new_L == L+1:
		M.append(i)
		L = new_L
	else:
		M[new_L] = i
		
	
	#print 'L = ', L
	#print M
	#print pred
	return M,pred,L


def find_longest_sub(X): # finds longest increasing subsequence of X
	M = [0] # list of 
	pred = [] # list of predecessors
	
	M.append(0)
	pred.append('none')
	L=1
	for i in range(1, len(X)):
		
		M,pred, L = extend(X,M, pred, i, L)
		
	ans = []
	last = M[L]
	ans.insert(0, X[last])
	for j in range(0, L-1):
		last = pred[last]
		ans.insert(0, X[last])
	#print ans
	return ans

# naive algorithms seem quite slow
# algorithm stolen from wikipedia

	
filename = 'rosalind_lgis.txt'

with open(filename, 'r') as input_file:
	temp = input_file.readline()
	n = int(temp.strip())
		
	temp = input_file.readline()
	temp = temp.strip()
	temp = temp.split()
	X = [int(x) for x in temp]
	
#print n
#print X



inc = find_longest_sub(X)
for x in inc:
	print x,
	
#dec = -1 *find_longest_sub(-1 *X)

print
Y = [0]*len(X)
for i in range(0, len(X)):
	Y[i] = -X[i]
temp = find_longest_sub(Y)
dec = [0] *len(temp)
for i in range(0, len(dec)):
	dec[i] = -temp[i]
for x in dec:
	print x,