#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *



filename = 'rosalind_2b.txt'

dna, prot = read_two_strings(filename)


m = len(prot)
L = len(dna)

for j in range(0, L - 3 * m + 1):
	w = dna[j: j + 3*m]
		
	if dna2prot(w) == prot:
		print w
	
	
	
dna = rev_comp(dna)
for j in range(0, L - 3 * m + 1):
	w = dna[j: j + 3*m]
		
	if dna2prot(w) == prot:
		print rev_comp(w)

	

		


