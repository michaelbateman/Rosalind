#Given: A DNA string s of length at most 1 kbp in FASTA format.

#Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

# BEWARE:  easy to forget to read the reverse complement, but this is necessary


import sys
import scipy.misc




    
    
    

def rev_comp(dna):
	rev_comp = ''
	
	comp = { 'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
	
	L = len(dna)
	i = 1
	
	while i <= L:
	    	rev_comp = rev_comp + comp[dna[-i]]
    		i +=1
	return rev_comp

def ham(s,t):
	ctr = 0
	for j in range(0, len(s)):
		if s[j] != t[j]:
			ctr +=1
			
	return ctr

s = 'rosalind_corr.txt'

try:
    input_file = open(s, "r")
    #print "input file is", input_file.name
except IOError:
    print "Oh no, we couldn't open our file!"


sample_dict = {}
temp = ''
sample = ''

for line in input_file:
    if '>' in line:	
	temp = line.rstrip()
	sample = temp.lstrip('>')
	#print 'SAMPLE:  ', temp2
	my_dna = ''
    else:
	my_dna = my_dna + line.strip()
	sample_dict.update({ sample: my_dna })
	

correct_list = []
for sam1 in sample_dict:
	is_correct = 0
	s = sample_dict[sam1]
	#print s
	
	for sam2 in sample_dict:
		t = sample_dict[sam2]
		if s == t and sam1 != sam2:
			is_correct = 1
			#print 'yes'
		elif s == rev_comp(t) and sam1 != sam2:
			is_correct = 1
		else: pass
		
	#print correct_list
	if is_correct == 1 : correct_list.append(sam1)

#print correct_list

for sam1 in sample_dict:
	s = sample_dict[sam1]
	if sam1 in correct_list: pass
	else:
		for sam2 in correct_list:
			t = sample_dict[sam2]
			#print s, t, rev_comp(t)
			if ham(s,t) == 1:
				print s + '->' + t
				break
			elif ham(s, rev_comp(t)) == 1:
				print s + '->' + rev_comp(t)
				break
			
			
		
	
		
			

