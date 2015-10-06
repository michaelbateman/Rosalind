#Given: A positive integer n < 10^5 and an array of length < = n.

#Return: the median

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




def smallest(A,k): # input array A and int k, output the kth smallest element of A
	#print k
	#print A
	j = randrange(len(A))
	#print j
	[X,Y,Z] = three_partition(A, j )
	#print X, Y, Z
	
	if k <= len(X):
		#print X, k
		return smallest(X,k)
	if k > len(X) + len(Y):
		#print k - len(X)
		#print Z, k - len(X) - len(Y)
		return smallest(Z, k - len(X) - len(Y) )
	else:
		#print
		#print j, Y[0]
		#print
		return Y[0]



s = 'rosalind_ps.txt'

with open(s, 'r') as input_file:

	temp = input_file.readline()
	n = temp.strip()
	temp = input_file.readline()
	T = temp.strip()
	L = T.split()
	A = []
	for x in L:
		A.append(int(x))
	temp = input_file.readline()
	k = int(temp.strip())
	






for j in range(1, k+1):
	print smallest(A,j),

