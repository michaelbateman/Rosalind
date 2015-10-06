#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *





filename = 'rosalind_4b.txt'

my_list = []
with open(filename, 'r') as in_file:
	for line in in_file:
		my_list.append(line.strip())
		
		

ans = {}

for s in my_list:
	for t in my_list:
		if s[1:] == t[:-1]:
			ans.update({s:t})
			
A = sorted(list(ans.keys()))
for s in A:
	print s, '->', ans[s]