
# Given : an integer n <= 10 ^ 5 and an array of n integers
# Return : a sorted array


import numpy as np

s = 'rosalind_par3.txt'



with open(s, 'r') as input_file:
	
	#n = [int(x) for x in input_file.readline().split()]
	temp = input_file.readline()
	temp2 = temp.strip()
	n = int(temp2)
	A = [int(x) for x in input_file.readline().split()]
	

	#print n
	#print A
	

def three_partition(A):
	B = [A[0]]
	#print A
	#print B
	location = 0
	for i in range(1, len(A)):
		#print A[0]
		#print A[i]
		#print B
		if A[i] > A[0]:
			#print ' case >'
			B.append(A[i])
		elif A[i] < A[0]:
			B.insert(0, A[i])
			location +=1
			#print ' case  < = '
		elif A[i] == A[0]:
			B.insert(location+1, A[i])
		else:
			return 'help me'
		
	return B



A = three_partition(A)


for i in range(0, len(A)):
	print A[i],

#print
#print is_sorted(A)


