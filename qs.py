#Given: A positive integer n < 10^5 and an array of length < = n.

#Return: sorted array  (should be done with quick sort)

from random import randrange
import numpy as np
import sys
sys.setrecursionlimit(10000)


def three_partition(A,j): # returns 3-partition using elt at index j as the pivot
	#print A
	A[0], A[j] = A[j], A[0]
	#print A
	B_less =[]
	B_equal = [A[0]]
	B_greater = []
	for i in range(1, len(A)):
		#print A[0]
		#print A[i]
		#print B
		if A[i] > A[0]:
			#print ' case >'
			B_greater.append(A[i])
		elif A[i] < A[0]:
			B_less.append(A[i])
			#print ' case  < = '
		elif A[i] == A[0]:
			B_equal.append(A[i])
		else:
			return 'help me'
		
	
	
	return [B_less, B_equal, B_greater]


def quick_sort(A): # sorts array A using quick sort
	#print A
	if len(A) <= 1:
		return A
	j = randrange(len(A))
	[X,Y,Z] = three_partition(A, j )
	return quick_sort(X) + Y + quick_sort(Z)
	
s = 'rosalind_qs.txt'

with open(s, 'r') as input_file:


	#line 1, length of array
	temp = input_file.readline()
	n = temp.strip()
	
	#line 2, array
	temp = input_file.readline()
	T = temp.strip()
	L = T.split()
	A = []
	for x in L:
		A.append(int(x))
	
	

#print A

A = quick_sort(A)
for x in A:
	print x,

