#Given: A protein string of length at most 1000 aa.

#Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)


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
    
prot = sys.argv[1]
inv_dict = {}
for a in genetic_code.values():
    ctr = 0
    for s in genetic_code:
	if genetic_code[s] == a:
	    ctr += 1
	else:
	    pass
    inv_dict.update({a:ctr})
    
ans = 1
for a in prot:
    temp = ans * inv_dict[a]
    ans = temp % 1000000  # modulo one million
    
temp = ans * 3 # to account for the three possibilities for the stop codon
ans = temp % 1000000  # modulo one million
print ans