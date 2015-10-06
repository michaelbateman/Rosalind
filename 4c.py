#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *





filename = 'rosalind_4c.txt'


with open(filename, 'r') as in_file:
	temp = in_file.readline()
	temp = temp.strip()
	k = int(temp) - 1
	
	temp = in_file.readline()
	s = temp.strip()
	
ans = {}
L = len(s)
for j in range(0, L  - k ):
	w = s[j:j+k]
	v = s[j+1:j+1+k]
	if w in ans:# and ans[w] != v:
		ans[w] = ans[w] + ',' + v
	else:
		ans.update({w: v})
	      
A = sorted(list(ans.keys()))
for s in A:
	print s, '->', ans[s]