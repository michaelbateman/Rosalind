#Given: A protein string P of length at most 1000 aa.

#Return: The total weight of P. Consult the monoisotopic mass table.


import sys
import scipy.misc



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


import sys

mass_dict = make_dict('mass_file.txt')

prot = sys.argv[1]

total = 0

for a in prot:
    total += mass_dict[a]
print total