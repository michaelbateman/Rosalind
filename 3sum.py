

import numpy as np






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
									
         

def is_sorted(B):
	# Notice this returns 'yes' if B has one element
	for i in range(0, len(B) - 1):
		if B[i] <= B[i+1]:
			pass
		else:
			return 'no'
	return 'yes'

def merge(B,C):
	for i in range(0, len(B)):
		#print 'find =', find(B[i], C)
		C.insert( find(B[i], C), B[i] )
		#print 'C = ', C
	return C

def merge_sort(A):
	#print A
	#print is_sorted(A)
	while is_sorted(A) == 'no':
		if len(A) == 2:
			B = A[:1]
			C = A[-1:]
	#		print B
	#		print C
		else:
			B = A[:len(A)/2]
			C = A[len(A)/2:]
			#print B
			#print C
		# Notice that is_sorted(B) is yes if B has one element
		if is_sorted(B) == 'no':
			A[:len(A)/2] = merge_sort(B)
			#print 'hi'
		elif is_sorted(C) == 'no':
			A[len(A)/2:] = merge_sort(C)
			#print 'hello'
		else:
			A = merge(B,C)
			#is_sorted(A) == 'yes'
			#break
			#print 'A is ', A
		
	return A		
	


def scan(A, m, k, n):
	for j in range(0, n):
		if A[j]  == - m - k:
			return j
	return -1



def zero_sum_three(A,n):
	#print(A)
	
	
	# algorithm stolen from wikipedia
	# previous version used a binary search and may have even been cubic? 
	# or at least n^2 log n
		
	for i in range(0, n):
		#print i
		start = i+1
		end = n-1
		#a = A[i]
		#b = A[start]
		#c = A[end]
		temp = -A[i]
		while start < end:
			#print 'length (A) = ', len(A)
			#print start
			#print end
			
			b = A[start]
			c = A[end]
			if b + c < temp:
				start = start +1
				
			elif b + c > temp:
				end = end - 1
				
			else :
				return [i, start, end]
			
			
		
		
	return [-1]


s = 'rosalind_3sum.txt'


with open(s, 'r') as input_file:
	
	
	k,n = [int(x) for x in input_file.readline().split()]
	#print input_file.readline()
	
	for line in input_file:
		
		A = [int(x) for x in line.split()]
		#print A
		B = np.sort(A)
		C = np.argsort(A)
		
		L = zero_sum_three(B, n)					
		if len(L) > 1:
			[i,j,k] = L
			[a,b,c] = merge_sort([C[i], C[j], C[k]])
			print a+1, b+1, c+1
		else:
			print -1
		