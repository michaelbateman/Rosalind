
import numpy as np

s = 'rosalind_pdst.txt'

try:
    input_file = open(s, "r")
    #print "input file is", input_file.name
except IOError:
    print "Oh no, we couldn't open our file!"




sample_dict = {}
temp = ''
sample = ''

index = 0

for line in input_file:
    if '>' in line:
	
	index +=1
	temp = line.rstrip()
	sample = temp.lstrip('>')
	#print 'SAMPLE:  ', temp2
	my_dna = ''
    else:
	my_dna = my_dna + line.strip()
	sample_dict.update({ index : my_dna })
	

#for sample in sample_dict:
    #print sample
    #print ''
    #print sample_dict[sample]
    #print ''
    #print ''
    
    
def ham(s,t):
	ctr = 0
	for j in range(0, len(s)):
		if s[j] != t[j]:
			ctr +=1
			
	return ctr

L = len(sample_dict[1])
    
print L
print sample_dict
for i in range(1, len(sample_dict)+1):
	string = ''
	for j in range(1, len(sample_dict)+1):
		#temp = (1.0 / float(L)) * ham(sample_dict[sam1], sample_dict[sam2])
		temp =  ham(sample_dict[i], sample_dict[j]) / float(L)
		#temp + = .00001
		#temp *= 10000
		#temp2 = int(temp)
		#temp = temp2 / float(
		#new = np.ceil(temp*10000) / 10000 
		#new += .00005
		#if temp < .001: temp = int(temp)	
		print temp,
		string += str(temp) + ' '
	#print string
	print 