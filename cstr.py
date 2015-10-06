#Given: A collection of at most 100 characterizable DNA strings, each of length at most 300 bp.

#Return: A character table for which each nontrivial character encodes the symbol choice at a single position of the strings. (Note: the choice of assigning '1' and '0' to the two states of each SNP in the strings is arbitrary.)



import sys
import numpy as np
import string

filename = 'rosalind_cstr.txt'


my_strings = []

with open(filename, 'r') as in_file:
	for line in in_file:
		temp = line.strip()
		my_strings.append(temp)
		

L = len(my_strings[0])

M = len(my_strings)
reference = my_strings[0]

char_dict = {}

group_0 = [] # here we write a 1 for the 'reference' string allele, just to match the example at rosalind
group_1 = []
	

for j in range(0, L):
	temp = ''
	temp_complement = ''
	ctr = 0
	for i in range(0, M):
		current = my_strings[i]
		if current[j] == reference[j]:
			ctr +=1
			temp += '1'
			temp_complement += '0'
		else:
			temp += '0'
			temp_complement += '1'
	
	if temp	in char_dict or temp_complement in char_dict:
		pass
	elif ctr <= 1 or ctr >= M-1:
		pass
	else:
		char_dict.update({j:temp})
		
		
for j in char_dict:
	print char_dict[j]