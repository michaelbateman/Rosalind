#Given: An integer n, followed by n protein strings, followed by a multiset of positive numbers (corresponding to the complete spectrum of some unknown protein string).

#Return: the maximum multiplicity of R - S[s_k], where S[s_k] is spectrum of s_k, k is kth string.
#	max is over both k and argument of R - S[s_k]

import sys
import scipy.misc
import numpy as np
import time

def make_dict(s):
    try:
        input_file = open(s, "r")
        #print "input file is", input_file.name
    except IOError:
        print "Oh no, we couldn't open our file!"

    dict = {}
    for line in input_file:
	temp = line.split()
	dict.update(  {temp[0]:float(temp[1])}  )
	
    return dict	

def mass(prot):
	total = 0
	for a in prot:
   		total += mass_dict[a]
	return total

def make_spectrum(prot): # inputs a protein, outputs its complete spectrum
	ans = []
	for j in range(0, len(prot)):
		ans.append(mass(prot[:j]))
		ans.append(mass(prot[j:]))
	return ans	
	
def convolve(A,B): # input is two lists, output is max of A convolved with B (subtraction)
	#print A
	#print B
	ans = 0
	conv_dict = {}
	#for a in A:
		#for b in B:
			#found = 0
			#for x in conv_dict:
				#if abs(a-b-x) < .01:
					#conv_dict[x] +=1
					#found = 1
					#break
				#else:
					#pass
			#if found == 0:
				#conv_dict.update({a-b:1})
			#else:
				#pass
	my_list = []
	for a in A:
		for b in B:
			my_list.append(a-b)
	my_list.sort()
			
	N = len(my_list)
	my_set = set()
	my_set.add(my_list[0])
	current_elt = my_list[0]
	i = 0
	while i < N:
		#print i, N, len(A), len(B)
		j = 0 
		while i+j < N and my_list[i+j] - my_list[i] <= .01:
			j+=1
		conv_dict.update({my_list[i]:j})
		i = i+j
			
	
	#A.sort()
	#B.sort()
	#M = len(A)
	#N = len(B)
	#my_list.sort()
	#i = 0
	#j = 0
	#for x in my_list:
		#conv_dict.update({x:0})
		#while i < M and j < N:
			#diff = A[i]-B[j]-x
			#if diff <=  - .01:
				#i+=1
			#elif diff >= .01:
				#j+=1
			#else:
				#conv_dict[x]+=1
				#if j< N-1 and abs(B[j+1] - B[j])< .01:
					#j+=1
				#else:
					#i +=1
					
	
	return conv_dict
	


end = time.clock()	
mass_dict = make_dict('mass_file.txt')

filename = 'rosalind_prsm.txt'

prot_dict = {} 

mass_list = [] # L is the list of partial protein masses

with open(filename, 'r') as input_file:
	n = input_file.readline()
	n = n.strip()
	n = int(n)
	for i in range(0, n):
		temp = input_file.readline()
		my_prot = temp.strip()
		#print temp
		prot_dict.update({my_prot:make_spectrum(my_prot)})
		
	for line in input_file:
		temp = float(line.strip())
		mass_list.append(temp)
		

max_mult = 0
max_prot_list = []

for prot in prot_dict:
	newtime = time.clock()
	#print 'everything else took', newtime - end, 'seconds'
	#print prot
	#print prot_dict[prot]
	#print mass_list
	#print 'aaaaaaaaaaaa'
	start =   time.clock() 
	conv_dict = convolve(prot_dict[prot], mass_list)
	#print conv_dict
	end = time.clock()
	#print 'convolving took', end - start, 'seconds'
#	print max(conv_dict.values()), prot
	M = max(conv_dict.values()) 
	if M > max_mult:
		max_mult = M
		max_prot_list = [prot]
	elif M== max_mult:
		max_prot_list.append(prot)
	else:
		pass
	
print max_mult
#print max_prot_list 
print max_prot_list[0]
	


#L = np.sort(L)
#diff = [0] * ( len(L) - 1)
#prot = ''
#for i in range(0, len(L)-1):
	#diff[i] = L[i+1] - L[i]
	#for x in mass_dict:
		#if abs(mass_dict[x] - diff[i]) < .01:
			#prot+=x
			#break

#print prot

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