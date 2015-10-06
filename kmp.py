#Given: A DNA string s (of length at most 100 kbp) in FASTA format.

#Return: The failure array of s.


import sys


s = 'rosalind_kmp.txt'

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
	sample_dict.update({ 0: my_dna })
	


s = sample_dict[0]

P = '0 '
previous = 10
for k in range(1,len(s)):
	temp = 0
	for L in range(1,  k+1 ):
	
		if L > previous + 5:
			break
		#print s[k+1-L:k+1]
		#print s[:L]
		#print
		#print
		if s[k+1-L:k+1] == s[:L]:
			temp = L
			
	previous = temp
	P = P+str(temp) + ' '
		
print P
#print len(s)
#print len(P)