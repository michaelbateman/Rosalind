#Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

#Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

import math
import sys

print ''
print ''
print ''
print ''

rna = sys.argv[1]

A_num = 0
C_num = 0

for j in range(0, len(rna)):
    if rna[j] == 'A':
	A_num +=1
    elif rna[j] == 'C':
	C_num +=1
	

print math.factorial(A_num)*math.factorial(C_num)

