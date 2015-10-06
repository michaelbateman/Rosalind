#Given: A DNA string Pattern.

#Return: The reverse complement of Pattern.

import sys
import scipy.misc
import numpy as np

from rosalind_functions import *




filename = 'rosalind_1c.txt'

sub, s = read_two_strings(filename)


L = find_occurrences(sub,s)

for j in range(0, len(L)):
	print L[j],

