#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *





filename = 'rosalind_4a.txt'

with open(filename, 'r') as in_file:
	temp = in_file.readline()
	temp = temp.strip()
	k = int(temp)
	
	temp = in_file.readline()
	s = temp.strip()

my_list = []
L = len(s)
for j in range(0, L+1 - k):
	my_list.append(s[j: j+k])
	
my_list.sort()

for x in my_list:
	print x