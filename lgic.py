#Given: A positive integer n<=10000 followed by a permutation pi of length n.

#Return: A longest increasing subsequence of pi, followed by a longest decreasing subsequence of pi.


import numpy as np
import sys
sys.setrecursionlimit(10000)


	
filename = 'rosalind_bip.txt'

with open(filename, 'r') as input_file:
	temp = input_file.readline()
	n = int(temp.strip())
	
	temp = input_file.readline()
	X = [int[x] for x in temp.strip()
	
	print n
	print X
	