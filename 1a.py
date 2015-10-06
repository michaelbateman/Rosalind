#Given: A DNA string Text and an integer k.

#Return: All most frequent k-mers in Text (in any order).

import sys
import scipy.misc
import numpy as np


def occurences(s,w):	# nice code stolen from http://stackoverflow.com/questions/2970520/string-count-with-overlapping-occurrences
	
	ctr = 0
	start = 0
	
	while True:
		start = s.find(w,start) + 1
		if start > 0:
			ctr +=1
		else:
			return ctr	



filename = 'rosalind_1a.txt'

with open(filename, 'r') as input_file:
	temp = input_file.readline()
	s = temp.strip()
	
	temp = input_file.readline()
	temp = temp.strip()
	k = int(temp)

kmers = ['']
bases = ['A', 'C', 'G', 'T']
j =0 
for i in range(0, k):
	new = []
	for w in kmers:
		for b in bases:
			new.append(w + b)
			#print w+b, k
						
	kmers = new
	
	
	
max_count = 0
max_list = []
ind = 0
for w in kmers:
	#if ind % 10000 == 0:
	#	print ind
	ind +=1
	c = occurences(s,w)
	#print w, c
	if c > max_count:
		max_list = [w]
		max_count = c
	elif c == max_count:
		max_list.append(w)
	else:
		pass

print len(kmers)
print max_count
for w in max_list:
	print w,
