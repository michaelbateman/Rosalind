#Given: A protein string P of length at most 1000 aa.

#Return: The total weight of P. Consult the monoisotopic mass table.


import sys
import scipy.misc
import numpy as np


def make_dict(s):
    try:
        input_file = open(s, "r")
        print "input file is", input_file.name
    except IOError:
        print "Oh no, we couldn't open our file!"

    dict = {}
    for line in input_file:
	temp = line.split()
	dict.update(  {temp[0]:float(temp[1])}  )
	
    return dict	




mass_dict = make_dict('mass_file.txt')

filename = 'rosalind_spec.txt'

L = [] # L is the list of partial protein masses

with open(filename, 'r') as input_file:
	for line in input_file:
		a = line.strip()
		a = float(a)
		L.append(a)
		

L = np.sort(L)
diff = [0] * ( len(L) - 1)
prot = ''
for i in range(0, len(L)-1):
	diff[i] = L[i+1] - L[i]
	for x in mass_dict:
		if abs(mass_dict[x] - diff[i]) < .01:
			prot+=x
			break

print prot

# Some extra code below to determine the possible differences in masses for an amino acid
# it appears that .01 is appropriate to discriminate amino acids of different masses.
# if the masses are different, then they are different by > .03

#differences = []

#for x in mass_dict:
	#for y in mass_dict:
		#if y != x: differences.append(abs(mass_dict[x] - mass_dict[y]))
		
		
#differences =  np.sort(differences)
#for i in range(0, len(differences)):
	#print differences[i]