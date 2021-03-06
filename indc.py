
#Given: Positive integer n 
#Return: array A of length 2n containing common log of  the probability that two diploid siblings share at least k of 2n chromosomes


import sys
import numpy as np
import scipy.misc


n = int(sys.argv[1])
#m = int(sys.argv[2])


def sum_of_bin(n, m):

	# Here m will play the role of k in the problem statement
	# This is the solution to the problem aspc, which computes sums of binomial coeffs via pascal's triangle
	L = [1,1]
	for j in range(2, n+1):
		new = [0]*(j+1)
		for k in range(0, j+1):
			if k == 0 or k == j:
				new[k] = 1
			else:
				new[k] = ( L[k] + L[k-1] ) 
			
		L = new
	
	total = 0
	for k in range(m, n+1):
		total += L[k]
	return total 
	

for k in range(1, 2*n+1):
	#print 2**(2*n), sum_of_bin(2*n, k), np.log10(sum_of_bin(2*n, k))
	if abs(np.log10(2**(-2*n) *sum_of_bin(2*n, k))) < .001:
		print 0,
	else:
		print  np.log10(2**(-2*n) *sum_of_bin(2*n, k)),





