#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *





filename = 'rosalind_4d.txt'


my_list = []
with open(filename, 'r') as in_file:
	for line in in_file:
		my_list.append(line.strip())
		
		
my_dict = {}

for s in my_list:
	w = s[:-1]
	v = s[1:]
	if w in my_dict:
		my_dict[w] = my_dict[w] + ',' + v
	else:
		my_dict.update({w:v})
		
	      
A = sorted(list(my_dict.keys()))
for s in A:
	print s, '->', my_dict[s]