#Given: A DNA string s of length at most 1 kbp in FASTA format.

#Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

# BEWARE:  easy to forget to read the reverse complement, but this is necessary


import sys

    
    
    

def rev_comp(dna):
    temp = ''
    comp = { 'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
    L = len(dna)
    i = 1
    while i <= L:
        temp = temp + comp[dna[-i]]
        i +=1
    return temp

def rev_pal(s):
    t = rev_comp(s)
    if s == t:
	return 'yes'
    else:
	return 'no'

s = 'rosalind_revp.txt'

try:
    input_file = open(s, "r")
    print "input file is", input_file.name
except IOError:
    print "Oh no, we couldn't open our file!"


sample_dict = {}
temp = ''
sample = ''

########  For use in reading a one line FASTA

for line in input_file:
    if '>' in line:	
	temp = line.rstrip()
	sample = temp.lstrip('>')
	#print 'SAMPLE:  ', temp2
	my_dna = ''
    else:
	my_dna = my_dna + line.strip()
	sample_dict.update({ 0: my_dna })
	

x = sample_dict[0]

#############################################

dna = sample_dict[0]
for j in range(0, len(dna)):
    for k in range(4, 12+1):
	#print j+1, k, len(dna),  '******'
	if rev_pal(dna[j:j+k]) == 'yes':
	    if j+k <= len(dna):		
	        print j+1, k#, dna[j:j+k], rev_comp(dna[j:j+k])
		#print j + k, len(dna)
	    else:
		#print j+1, k, dna[j:j+k], rev_comp(dna[j:j+k]), '**********'
		#print j + k, len(dna)
		pass
	else:
	    pass



