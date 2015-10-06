#Given: A collection of at most 100 characterizable DNA strings, each of length at most 300 bp.

#Return: A character table for which each nontrivial character encodes the symbol choice at a single position of the strings. (Note: the choice of assigning '1' and '0' to the two states of each SNP in the strings is arbitrary.)



import sys
import numpy as np
import string

n = int(sys.argv[1])

temp = 1
for j in range(3, n+1):
	temp *= 2*j - 5
	temp = temp % 1000000
	#print temp
	
print temp
	