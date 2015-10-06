#Given: A string Text as well as integers k and d.

#Return: All most frequent k-mers with up to d mismatches in Text.

import sys
import scipy.misc
import time
import numpy as np

from rosalind_functions import *


filename = 'rosalind_1h.txt'


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
print 'Making kmers'
kmer_dict = {}
rev_kmer_dict = {}
for i in range(0, k):
	new = []
	for w in kmers:
		for b in bases:
			new.append(w + b)
			#print w+b, k
						
	kmers = new

for w in kmers:
	kmer_dict.update({w:0})
	rev_kmer_dict.update({w:0})



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
	v = rev_comp(w)
	big_ball_1 = ball(set([w]), d)
	big_ball_2 = ball(set([v]), d)
	#big_ball = big_ball_1.union(big_ball_2)
	
	for x in big_ball_1:
		kmer_dict[x] += 1
	
	for x in big_ball_2:
		rev_kmer_dict[x] += 1
			
	#for w in big_ball_1:
		#if w in kmer_dict:
			#kmer_dict[w] += 1
		#else:
			#kmer_dict.update({w : 1}) 
	#for w in big_ball_2:
		#if w in rev_kmer_dict:
			#rev_kmer_dict[w] += 1
		#else:
			#rev_kmer_dict.update({w : 1}) 

max_count = 0
max_list = []
ind = 0
for w in kmers:
	#if ind % 10000 == 0:
		#print ind
	ind +=1
	c = kmer_dict[w] + rev_kmer_dict[w]
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





