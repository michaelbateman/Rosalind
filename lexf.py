#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

#Return: All strings of length n that can be formed from the alphabet, ordered lexicographically..

import sys
import scipy.misc

s = sys.argv[1]
n = int(sys.argv[2])

my_symbols = s.split()

L = ['']

for j in range(0, n):
    temp = []
    for w in L:
	for a in my_symbols:
	    temp.append(w+a)
    L = temp


#print 'n factorial is ', len(L)
#print 
#print
#print


for w in L:
    print w