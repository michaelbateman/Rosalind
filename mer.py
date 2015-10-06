

import numpy as np

s = 'rosalind_mer.txt'


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
         


with open(s, 'r') as input_file:
	
	#n = [int(x) for x in input_file.readline().split()]
	temp = input_file.readline()
	temp2 = temp.strip()
	n = int(temp2)
	A = [int(x) for x in input_file.readline().split()]
	
	temp = input_file.readline()
	temp2 = temp.strip()
	m = int(temp2)
	B = [int(x) for x in input_file.readline().split()]
	
	#print n
	#print A
	#print m
	#print B
	
	
#print A
for i in range(0, m):
	#print find(B[i], A)
	A.insert( find(B[i], A), B[i] )
	#print A
	
for i in range(0, len(A)):
	print A[i],


