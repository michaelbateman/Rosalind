#Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

#Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

import numpy as np






s = 'rosalind_sseq.txt'

try:
    input_file = open(s, "r")
    print "input file is", input_file.name
except IOError:
    print "Oh no, we couldn't open our file!"

sample_dict = {}
temp = ''
sample = ''

num = 0

for line in input_file:
    if '>' in line:
	num +=1
	
	temp = line.rstrip()
	sample = temp.lstrip('>')
	#print 'SAMPLE:  ', temp2
	my_dna = ''
    else:
	my_dna = my_dna + line.strip()
	sample_dict.update({ num: my_dna })
	

s = sample_dict[1]
t = sample_dict[2]
L = []
ind = 0
for j in range(0, len(s)):
        #print j, len(s), ind, len(t)
	if ind >= len(t):
	    break
        elif s[j] == t[ind]:
            L.append(j+1)
	    ind +=1
	    #print L
        else:
            pass
    
ans = ''
for x in L:
    ans+= str(x) + ' '

print ans
