
# Given : an integer n <= 10 ^ 5 and an array of n integers
# Return : a sorted array


import numpy as np

s = 'rosalind_ms.txt'


def find(k, A):
        bot =0
        top = len(A)
      	if k < A[0]: return 0
	if k > A[len(A)-1]: return len(A)
        while bot +1 < top:
                
                mid = (bot + top)  / 2
        #       print ' k = ' , k
        #       print ' A[mid] = ', A[mid]
                if A[mid] == k: return mid 
                elif A[mid]< k: 
			bot = mid
			if bot +1 == top: 
				return top
                elif A[mid] > k: 
			top = mid 
			if bot +1 == top: 
				return top
         

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
		#print find(B[i], A)
		C.insert( find(B[i], C), B[i] )
		#print A
	return C

with open(s, 'r') as input_file:
	
	#n = [int(x) for x in input_file.readline().split()]
	temp = input_file.readline()
	temp2 = temp.strip()
	n = int(temp2)
	A = [int(x) for x in input_file.readline().split()]
	

	#print n
	#print A
	
	
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
		# Notice that is_sorted(B) is yes if B has one element
		if is_sorted(B) == 'no':
			A[:len(A)/2] = merge_sort(B)
		elif is_sorted(C) == 'no':
			A[len(A)/2:] = merge_sort(C)
		else:
			A = merge(B,C)
			#is_sorted(A) == 'yes'
			#break
			#print 'A is ', A
		
	return A		
	

A = merge_sort(A)

for i in range(0, len(A)):
	print A[i],

#print
#print is_sorted(A)


