
import numpy as np
import sys
from rosalind_functions import *


def read_scoring_matrix(filename): # reads blosum62 matrix from filename
	
	with open(filename, 'r') as in_file:
		temp = in_file.readline()
		temp = temp.strip()
		index = temp.split()
		
		#A = [[0 for i in range(0, len(index))]  for j in range(0, len(index)) ]
		
		my_dict = {} # make a dictionary A to encode values
		i = 0
		for line in in_file:
			temp = line.strip()
			L = line.split()
			current = L.pop(0)
			j = 0
			for x in index:
				my_dict.update({ ( current, x ): int(L[j]) })
				#A[i][:] = [L[j] for j in range(0, len(L))]
				j+=1
			#i +=1
			
		return my_dict
	

filename = 'rosalind_loca.txt'
g = 5 # gap penalty
P = read_scoring_matrix('PAM250.txt')
#print P
#print P[('Y','Y')]


my_dict = read_fasta(filename)
#print my_dict[1]
#print my_dict[2]

max_align = 0
s = my_dict[0]
t = my_dict[1]
L = len(s)


#[dist_matrix, s_matrix, t_matrix] = edit_distance(my_dict[0],my_dict[1])
[max_score, max_S, max_T] = local_optimal_align(s,t, g, P)

print max_score
#print max_S
#print max_T

print compress(max_S)
print compress(max_T)

#print compress('ABCD------EFGH')
#print compress('-A-B-C-D-E-F-G-H')

#print s
#print
#print t