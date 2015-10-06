#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *



filename = 'rosalind_2c.txt'

prot = read_string(filename)

def total_mass(prot):
	N = len(prot)
	total =  0
	for j in range(0, N):
		total += mass_dict[prot[j]]
	return total

mass_dict = make_dict('mass_file.txt')

for a in mass_dict:
	mass_dict[a] = int(mass_dict[a])

L = len(prot)

spectrum = []

for j in range(0, L):
	p = prot[j:] + prot[:j]
	for i in range(1, L):
		spectrum.append(total_mass(p[:i]))

spectrum.append(0)
spectrum.append(total_mass(prot))

S = sorted(spectrum)

for m in S:
	print m,