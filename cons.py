#Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

#Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

import numpy as np

s = 'rosalind_cons.txt'

try:
    input_file = open(s, "r")
    print "input file is", input_file.name
except IOError:
    print "Oh no, we couldn't open our file!"




def gc( dna ):
    weight = {'A': 0, 'T': 0, 'C':1, 'G': 1} 
    total = 0 
    for base in dna:
	total = total + weight[base]
    #print total
    #print len(dna)
    #return 0
    if len(dna) == 0:
	return 0
    else:
	return (100.0 *   float(total) / float(len(dna))  )
	


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
    


L = len(sample_dict[sample])

#A = np.zeros((1,L))
#C = np.zeros((1,L))
#G = np.zeros((1,L))
#T = np.zeros((1,L))

A = []
C = []
G = []
T = []

for i in range(0,L):
    A.append(0)
    C.append(0)
    G.append(0)
    T.append(0)





consensus = ''

bases = ['A', 'C', 'G', 'T']
for i in range(0, L):
    for sample in sample_dict:
	print sample_dict[sample][i]
    	if sample_dict[sample][i] == 'A':
	    A[i] +=1
	elif sample_dict[sample][i] == 'C':
	    C[i] +=1
	elif sample_dict[sample][i] == 'G':
	    G[i] +=1
	elif sample_dict[sample][i] == 'T':
	    T[i] +=1
	else:
	    pass
    print i 
    
    temp = [A[i], C[i], G[i], T[i]]
    consensus = consensus + str( bases[np.argmax(temp)] )
    
    
print consensus
    
A_string = ''
for i in range(0,L):
    A_string = A_string + str(A[i]) + ' '

C_string = ''
for i in range(0,L):
    C_string = C_string +  str(C[i]) + ' '

G_string = ''
for i in range(0,L):
    G_string = G_string +  str(G[i]) + ' '

T_string = ''
for i in range(0,L):
    T_string = T_string +  str(T[i]) + ' '

t = 'cons_output.txt'
output_file = open(t, 'w')

output_file.write(consensus+ '\n')
output_file.write('A: '+ A_string+'\n')
output_file.write('C: '+ C_string+ '\n')
output_file.write('G: '+ G_string+ '\n')
output_file.write('T: '+ T_string+'\n')
print 'A:', A_string
print 'C:', C_string
print 'G:', G_string
print 'T:', T_string




    
print ''
print ''
print ''

    






