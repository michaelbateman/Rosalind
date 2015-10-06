#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *





filename = 'rosalind_2g.txt'

with open(filename, 'r') as in_file:
	temp = in_file.readline()
	temp = temp.strip()
	spec = [int(x) for x in temp.split()]
	
#print spec

A = []

for x in spec:
	for y in spec:
		if y < x:
			A.append(x-y)
			
B = set(A)
mult_dict = {}

for x in B:
	mult_dict.update({x:A.count(x)})

for x in mult_dict:
	m = mult_dict[x]
	for i in range(0,m):
		print x,
		
		