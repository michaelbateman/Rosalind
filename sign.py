#Given: A positive integer n<=6.

#Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).

import sys
import scipy.misc

n = int(sys.argv[1])

L = [[1], [-1]]

for m in range(2, n+1):
    temp = []
    for w in L:
	for i in range(0, m):
	    temp.append( w[0:i] + [str(m)] + w[i:m]   )
	    temp.append( w[0:i] + [str(-m)] + w[i:m]   )
    L = temp


#print 'n factorial is ', len(L)
#print 
#print
#print

print len(L)
for w in L:
    temp = ''
    for i in w:
	temp = temp +  str(i) + ' '
    print temp