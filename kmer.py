#Given: A DNA string s in FASTA format (having length at most 100 kbp).

#Return: The 4-mer composition of s.

import sys


s = 'rosalind_kmer.txt'

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
	






bases = ['A', 'C', 'G', 'T']

L = ['']

for i in [0,1,2,3]:
    temp = []
    for w in L:
	for a in bases:
	    temp.append(w+a)
    L = temp
    

def kmer(s,t):
    ctr = 0
    for j in range(0, len(s)):
	if s[j:j+4] == t:
	    ctr +=1
    return ctr
	
dna = sample_dict[sample]
#print dna
#print kmer(dna, 'CTTC')
ans = ''
for w in L:
    ans += str(kmer(dna, w)) + ' '
    
print ans