#Given: A DNA string Pattern.

#Return: The reverse complement of Pattern.

import sys
import scipy.misc
import numpy as np

from rosalind_functions import *




filename = 'rosalind_2a.txt'

s = read_string(filename)
print rev_comp(s)

