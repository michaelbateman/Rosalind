
#Given: Positive integer n 
#Return: array A of length 2n containing common log of  the probability that two diploid siblings share at least k of 2n chromosomes


import sys
import numpy as np
import scipy.misc



def can_extend(s,t): # return 'yes' if the kmer s and the kmer t overlap on the final k-1 bases of s
	#print s, t
	#print s[1:], t[:-1]
	if s[1:] == t[:-1]:
		#print 'yes'
		return 'yes'
	else:
		return 'no'


def circle(sub,dna): # accepts a substring and a circular dna and checks for inclusion
	x = len(sub)
	for j in range(0, len(dna) - x +1):
		#print 'testing', sub, 'with', dna[j:j+x]
		if sub == dna[j:j+x]: return 'yes'
		else: pass
	
	for k in range(1,x):
		#print 'testing', sub, 'with',dna[-k:] + dna[:x-k]
		if sub == dna[-k:] + dna[:x-k]: return 'yes'
		else: pass
	return 'no'

filename = 'rosalind_pcov.txt'

L = []
initial_list = []
with open(filename, 'r') as input_file:
	for line in input_file:
		L.append(line.strip())
		initial_list.append(line.strip())

L = set(L)
L = list(L)


current = L[0]
L.remove(current)
dna = current
while len(L)> 0:
	#print 'dna is', dna
	extendable = 'no'
	for t in L:
		if can_extend(current,t)  == 'yes' and t != current:
			dna = dna + t[-1]
			current = t
			L.remove(t)
			extendable = 'yes'
			break
		else:
			pass
			
	if extendable == 'no':
		print 'cannot extend further'
		break



#print dna
x = len(initial_list)
#print x
#print initial_list
dna = dna[0:len(initial_list)]
#print dna
print dna
# check correctness
status = 'PASS'
for sub in initial_list:
	if circle(sub, dna) == 'yes':
		pass
	else:
		print sub, 'is not in', dna
		status = 'FAIL'
		break
#print status
	

	



