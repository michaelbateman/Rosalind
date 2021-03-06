#Given: A positive integer n < 10^5 and an array of length < = n.

#Return: A sorted array

import numpy as np
import sys
sys.setrecursionlimit(10000)



def bubble(A, M):
	A.append(M)
	i = len(A) - 1
	#parent = (i + 1) / 2 - 1
	while A[(i + 1) / 2 - 1] < A[i] and i > 0:
		temp = A[i]
		A[i] = A[(i + 1) / 2 - 1]
		A[(i + 1) / 2 - 1] = temp
		i = (i + 1) / 2 - 1
	return A


def decapitate_and_sift(A):
	#print len(A)
	#print A
	A[0] = A[len(A)-1]
	del A[len(A)-1]
	i = 0
	if 2*i + 1 >= len(A):
		return A
	elif 2*i + 2 >= len(A):
		if A[i] < A[2*i + 1]:
			temp = A[i]
			A[i] = A[2*i+1]
			A[2*i+1] = temp
			return A
		else:
			return A
	while (A[i] < A[2*i+1] or A[i] < A[2*i+2]):
			if A[2*i + 2] < A[2*i+1]:
				temp = A[i]
				A[i] = A[2*i+1]
				A[2*i+1] = temp
				i = 2*i + 1			
				if 2*i + 1 >= len(A):
					return A
				elif 2*i + 2 >= len(A):
					if A[i] < A[2*i + 1]:
						temp = A[i]
						A[i] = A[2*i+1]
						A[2*i+1] = temp
						return A
					else:
						return A
			else:
				temp = A[i]
				A[i] = A[2*i+2]
				A[2*i+2] = temp
				i = 2*i + 2
				if 2*i + 1 >= len(A):
					return A
				elif 2*i + 2 >= len(A):
					if A[i] < A[2*i + 1]:
						temp = A[i]
						A[i] = A[2*i+1]
						A[2*i+1] = temp
						return A
					else:
						return A
				
	return A



s = 'rosalind_hs.txt'

with open(s, 'r') as input_file:

	temp = input_file.readline()
	n = temp.strip()
	for line in input_file:
		A = [int(x) for x in line.split()]
	#print n 
	#print A

B = [A[0]]

for i in range(1, len(A)):
	B = bubble(B, A[i])
	

sorted = []
for i in range(0, len(B)):
	sorted.append(B[0])
	B = decapitate_and_sift(B)
	
#print sorted



for i in reversed(sorted):
	print i,
