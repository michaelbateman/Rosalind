

import numpy as np

s = 'rosalind_ins.txt'


def swap(k, l, A):
	tempk = A[k]
	templ = A[l]
	A[k] = templ
	A[l] = tempk
	return A

with open(s, 'r') as input_file:
	
	#n = [int(x) for x in input_file.readline().split()]
	temp = input_file.readline()
	temp2 = temp.strip()
	n = int(temp2)
	#print n
	A = [0] * n
	#print A
	A = [int(x) for x in input_file.readline().split()]
	#print A
	
ctr = 0

for i in range(0, len(A)):
	j = i
	while ( j>0 and A[j] < A[j-1] ):
		#swap(A[j], A[j-1])
		temp = A[j]
		#temp1 = A[j-1]
		A[j] = A[j-1]
		A[j-1] = temp
		ctr +=1
		#print A
		j -=1
		

print ctr