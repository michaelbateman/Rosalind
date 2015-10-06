#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *



filename = 'rosalind_2a.txt'

rna = read_string(filename)
		
		
prot = rna2prot(rna)
print prot