#Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

#Return: The protein string encoded by s

import sys
s = sys.argv[1]



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
    
    
i = 0
prot = ''


for i in range(0, len(s)):
    if i % 3 == 0:
	    #print prot
	    codon = s[i] + s[i+1] + s[i+2]
	    if genetic_code[codon] == 'Stop':
		break
	    else:
	    	prot = prot + genetic_code[codon]
    else:
	pass
    

print ''
print ''
print ''
print prot