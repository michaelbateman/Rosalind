#Given: A DNA string Pattern.

#Return: The reverse complement of Pattern.

import sys
import scipy.misc
import numpy as np

from rosalind_functions import *



def extend_kmers(my_list):
	bases = ['A', 'C', 'G', 'T']
	for i in range(0, k):
		new = []
		for w in my_list:
			for b in bases:
				new.append(w + b)
				#print w+b, k
						
		kmer_list = new
	return kmer_list

filename = 'rosalind_1d.txt'

with open(filename, 'r') as in_file:
	temp = in_file.readline()
	s = temp.strip()
	
	temp = in_file.readline()
	temp = temp.strip()
	k,L,t = temp.split()
	k, L, t = int(k), int(L), int(t)

#print s
#print k, L, t

kmer_list = ['A', 'C', 'G', 'T']
for j in range(1, k):
	#print kmer_list
	kmer_list = find_clumps(L,t, s, kmer_list)
	#print 'number2'
	#print kmer_list
	kmer_list = extend_kmers(kmer_list)

kmer_list = find_clumps(L,t, s, kmer_list)

for w in kmer_list:
	print w,


