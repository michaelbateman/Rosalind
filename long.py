#Given: At most 50 DNA strings whose length does not exceed 1 kbp in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

#The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

#Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).



import numpy as np

s = 'rosalind_long.txt'

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
	



#for sample in sample_dict:
    #print sample
    #print ''
    #print sample_dict[sample]
    #print ''
    #print ''
    


n = len(sample_dict)

def concat(s,t):
    L = int( np.ceil( float(len(t)) / 2.0 ) )
    for j in range(L, len(t) + 1):
	if s[:j] == t[-j:]:
	    return t[:-j] + s
    for j in range(0, len(s) - len(t) ):
	if s[j:j + len(t)] == t:
	    return s
    for j in range(len(s) - len(t) , len(s) - L + 1):
	if s[j: ]== t[:len(s[j:])]:
	    return s + t[len(s[j:]):]

    return 'no'
    

s = sample_dict[sample]
del sample_dict[sample]
#print s

#for i in range(2,n+1):
    #L.append(i)

while len( sample_dict.keys() ) > 0:
    for sample in sample_dict.keys():
        t = sample_dict[sample]
        if concat(s,t) == 'no':
            pass
        else:
	    s = concat(s,t)
	    del sample_dict[sample]
	    #print s

print s