

import numpy as np

s = 'rosalind_2sum.txt'


def scan(A, m):
	for j in range(0, len(A)):
		if A[j] == -m:
			return j
	return -1



def zero_sum(A):
	#print(A)
	for i in range(0, len(A)):
		temp = scan(A, A[i])
		if temp >= 0 and i < temp:
			#print i, scan(A, A[i])
			return str(i+1) + ' ' + str(temp+1 )  
		if temp >= 0 and i > temp:	
			return str(temp+1 ) + ' ' +   str(i+1)
	return -1




with open(s, 'r') as input_file:
	
	
	k,n = [int(x) for x in input_file.readline().split()]
	
	
	for line in input_file:
		
		A = [int(x) for x in line.split()]
		#print A
		print zero_sum(A)		
		
		