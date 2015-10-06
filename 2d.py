#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *


m = int(sys.argv[1])


filename = 'rosalind_2d.txt'

#with open(filename, 'r') as in_file:
	#temp = in_file.readline()
	#temp = temp.strip()
	#m = int(temp)

mass_dict = make_dict('mass_file.txt')

for a in mass_dict:
	mass_dict[a] = int(mass_dict[a])



L = m / 57 + 1

f = [0]*(m+1)

#for n in range(0, 57):
	#f[n] = 0
f[0] = 1


X = list(set(mass_dict.values()))

for n in range(1, m + 1):
	#print 'hi, m = ', m
	total = 0
	#for a in mass_dict:
		#if mass_dict[a] == n:	total = total + 1
	
	for x in X:
		if n - x >=0: # and  f[n - mass_dict[a]] > 0:
		#	print n - mass_dict[a], f[n - mass_dict[a]]
			total = total + f[n - x] 
		#	print a, mass_dict[a], total, f[n - mass_dict[a]], n - mass_dict[a]
	f[n] = total
	#print n, f[n]
	
print f[m]
#print f[m-1]
#print f[m-2]

		
		