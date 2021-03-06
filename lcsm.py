#Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

#Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)


def Ext(w):
    ans = []
    for x in ['A', 'C', 'G', 'T']:
	ans.append(w + x)
    return ans
    
    
    
import numpy as np

s = 'rosalind_lcsm.txt'

try:
    input_file = open(s, "r")
    print "input file is", input_file.name
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
	



for sample in sample_dict:
    print sample
    print ''
    print sample_dict[sample]
    print ''
    print ''
    
    
    
    
    
    
    
    




common_match_exists = 1
L = ['']

while common_match_exists == 1:
    temp = []
    for w in L:
	for v in Ext(w):
	    ctr = 0
	    for sam in sample_dict:
		if v in sample_dict[sam]:
		    ctr +=1
		else:
		    break
	    if ctr == len(sample_dict):
		temp.append(v)
		
    if len(temp) == 0:
	print L
	common_match_exists = 0
    else:
	L = temp
		    
		    
		    