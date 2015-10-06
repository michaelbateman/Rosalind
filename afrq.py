
#Given: Positive integer n 
#Return: array A of length 2n containing common log of  the probability that two diploid siblings share at least k of 2n chromosomes


import sys
import numpy as np
import scipy.misc


def carriers(a): # a is proportion of population being homozygous recessive.  returns proportion carrying at least one copy of allele.  I.e., input is p^2, output is p^2 + 2pq
	p = np.sqrt(a)
	q = 1-p
	return p**2 + 2 * p * q


filename = 'rosalind_afrq.txt'

with open(filename, 'r') as input_file:
	L = input_file.readline()
	L = L.strip()
	L = [float(x) for x in L.split()]
	

	

length = len(L)
for i in range(0, length):
	print carriers(L[i]),


