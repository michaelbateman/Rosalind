#Given: A DNA string Pattern.

#Return: The reverse complement of Pattern.

import sys
import scipy.misc
import numpy as np

from rosalind_functions import *


filename = 'rosalind_1f.txt'


with open(filename, 'r') as in_file:
		temp = in_file.readline()
		sub = temp.strip()
		
		temp2 = in_file.readline()
		s = temp2.strip()
		
		temp3 = in_file.readline()
		d = int( temp3.strip() )
		
	


#print make_near_matches(sub, d)

#print neighbors(neighbors(neighbors('AAA')))
#print len(neighbors(neighbors(neighbors('AAA'))))
#print ball(set(['AAA']), 3)
#print len(ball(set(['AAA']), 3))

my_set = set()
print 'STARTED'
big_ball = ball(set([sub]),d)
print 'Made big ball'
for x in big_ball:
	my_set.update(find_occurrences(x, s))

print 'found occurrences'

temp = list(my_set)

#print temp
for a in sorted(temp):
	print a,
	       
#print sorted(temp)





