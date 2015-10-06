#Given: A DNA string Pattern.

#Return: The reverse complement of Pattern.

import sys
import scipy.misc
import numpy as np

from rosalind_functions import *


filename = 'rosalind_1e.txt'

s = read_string(filename)

C_count = 0
G_count = 0

skew = [0]
L = len(s)
min_indices = []
min_skew = 0
for j in range(0, L):
	if s[j] == 'C':
		C_count +=1
	elif s[j] == 'G':
		G_count +=1
	skew.append(G_count - C_count)
	if skew[j+1] < min_skew:
		min_indices = [j+1]
		min_skew = skew[j+1]
	elif skew[j+1] == min_skew:
		min_indices.append(j+1)
	#print skew[j+1]
for x in min_indices:
	print x,






