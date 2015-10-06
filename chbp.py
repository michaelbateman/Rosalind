#Given: A collection of at most 100 characterizable DNA strings, each of length at most 300 bp.

#Return: A character table for which each nontrivial character encodes the symbol choice at a single position of the strings. (Note: the choice of assigning '1' and '0' to the two states of each SNP in the strings is arbitrary.)



import sys
import numpy as np
import string

filename = 'rosalind_chbp.txt'


my_chars = []

with open(filename, 'r') as in_file:
	temp = in_file.readline()
	species_list = temp.split()
	for line in in_file:
		temp = line.strip()
		my_chars.append(temp)
		

M = len(species_list)
species_dict = {}
for m in range(0, M):
	species_dict.update({m: species_list[m]})

C = len(my_chars)

def is_sibling(m, n): # given two species (parameterized here by integers), determine whether they share a parent
			# this happens if and only if they are in all of the same nontrivial characters
	for i in range(0,C):
		#print m, len(my_chars)
		#temp1 = my_chars[m]
		#temp2 = my_chars[n]
		#print temp1
		#print m, n, i
		if my_chars[i][m] != my_chars[i][n]:
			return 'no'
	return 'yes'


def make_families(I): # I is a list of indices
			# returns all families 
	families = []
	for m in I:
		siblings = set()
		for n in I:
			
			if is_sibling(n,m) == 'yes':
				siblings.add(n)
			else:
				pass
		if siblings in families:
			pass
		else:
			families.append(siblings)
			
	return families


while len(I) > 

I = range(0, M)
print make_families(I)
		
		
			
		