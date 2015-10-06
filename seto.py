#Given: A positive integer n < 10^5 and an array of length < = n.

#Return: A sorted array


import numpy as np
import sys
sys.setrecursionlimit(10000)



def print_set(A):
	A = list(A)
	A = np.sort(A)
	for i in range(0, len(A)):
		if i == 0:
			print '{'+str(A[i])+',', 
		elif i < len(A) - 1:
			print str(A[i])+',',
		else:
			print str(A[i])+ '}'



def union(A,B):
	C = set()
	for y in A:
		C.add(y)
	#print_set(A)
	#print_set(B)
	#print 'hello'
	for x in B:
		#print x
		#print A
		if x in A:
			##print 'b'
			pass
		else:
			C.add(x)
	return C
	


def intersection(A,B):
	#print 'hello'
	C = set()
	for y in A:
		C.add(y)
	#print A
	#print B
	for x in A:
		if x in B:
			pass
		else:
			#print x
			C.remove(x)
	
	return C


def complement(A, U): # returns complement in universe U
	C = set()
	for y in U:
		C.add(y)
	for x in A:
		C.remove(x)
	return C	

def difference(A,B):
	C = set()
	for y in A:
		C.add(y)
	for x in B:
		if x in A:
			C.remove(x)
	#print 'a;lksdfj'
	return C




s = 'rosalind_seto.txt'

with open(s, 'r') as input_file:

	temp = input_file.readline()
	n = int(temp.strip())
	temp = input_file.readline()
	L = temp.strip()
	L = L.strip('{')
	L = L.strip('}')
	L = L.split(', ')
	
	A = []
	#print L
	for x in L:
		A.append(int(x))
	
	temp = input_file.readline()
	L = temp.strip()
	L = L.strip('{')
	L = L.strip('}')
	L = L.split(', ')
	
	B = []
	for x in L:
		B.append(int(x))
	
	A = set(A)
	B = set(B)





U = set()

for i in range(1, n+1):
	U.add(i)
	
#print U


#print (union(A,B))
#print (intersection(A,B))
#print (difference(A,B))
#print (difference(B,A))
#print (complement(A,U))
#print (complement(B,U))

#print_set(A)
#print_set(B)
#print

print_set(union(A,B))
print_set(intersection(A,B))
print_set(difference(A,B))
print_set(difference(B,A))
print_set(complement(A,U))
print_set(complement(B,U))




