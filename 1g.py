#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *


filename = 'rosalind_1g.txt'


with open(filename, 'r') as in_file:
		temp = in_file.readline()
		s = temp.strip()
		
		temp2 = in_file.readline()
		temp2 = temp2.strip()
		temp2 = temp2.split()
		k = int(temp2[0])
		d = int(temp2[1])
		
		
	

kmers = ['']
bases = ['A', 'C', 'G', 'T']
j =0 
#print 'Making kmers'
#for i in range(0, k):
	#new = []
	#for w in kmers:
		#for b in bases:
			#new.append(w + b)
			##print w+b, k
						
	#kmers = new

kmer_dict = {}
i =  0 	
#print 'finding kmers'
L = len(s)
start = time.clock()
for j in range(0, L - k + 1):
	if j%1000 == 0:
		#print j, float(j) / float(L)
		now = time.clock()
		#print now - start
	w = s[j:j+k]
	big_ball = ball(set([w]), d)
	for w in big_ball:
		if w in kmer_dict:
			kmer_dict[w] += 1
		else:
			kmer_dict.update({w : 1}) 


max_count = 0
max_list = []
ind = 0
for w in kmer_dict:
	#if ind % 10000 == 0:
		#print ind
	ind +=1
	c = kmer_dict[w]
	#print w, c
	if c > max_count:
		max_list = [w]
		max_count = c
	elif c == max_count:
		max_list.append(w)
	else:
		pass
	
#print max_count
for w in max_list:
	print w,

#for w in kmers:
	#i +=1
	#if i%10000 == 0: print i, float(i) / float(L)
	#find_occurrences(w, s)



#my_set = set()
#print 'STARTED'
#big_ball = ball(set([sub]),d)
#print 'Made big ball'
#for x in big_ball:
	#my_set.update(find_occurrences(x, s))

#print 'found occurrences'

#temp = list(my_set)

##print temp
#for a in sorted(temp):
	#print a,
	       
#print sorted(temp)





