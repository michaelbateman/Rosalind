#Given: A DNA string s of length at most 1 kbp in FASTA format.

#Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

# BEWARE:  easy to forget to read the reverse complement, but this is necessary


import sys
import scipy.misc



genetic_code = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    
    
dna_code = {}    

for s in genetic_code:
    temp = ''
    for i in range(0,3):
	if s[i] == 'U':
	    temp+='T'
	else:
	    temp+=s[i]
    dna_code.update({temp: genetic_code[s]})
    
    
    
    
    


s = 'rosalind_orf.txt'

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
	sample_dict.update({ 0: my_dna })
	


x = sample_dict[0]


Stop = ['TAA', 'TAG', 'TGA']

prot_list = []

print 
print
for j in range(0, len(x)):
    if x[j:j+3] == 'ATG':
	i = j 
	prot = ''
	reached_end = 0
        while x[i:i+3] not in Stop:
	    #print 'index is', i, 'out of', len(x)
	    if i < len(x):
		prot = prot + dna_code[x[i:i+3]]
	        i += 3
	        #print prot
	    else:
		reached_end = 1
		break
	if reached_end == 0:
	    prot_list.append(prot)
	else:
	    pass
    else:
	pass

dna = x

    
S = set(prot_list)

for s in S:
    print s