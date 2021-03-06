#Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

#Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.

import numpy as np
import sys
import scipy.misc

s = sys.argv[1]
t = sys.argv[2]

temp_A = t.split()
A = []
for i in range(0, len(temp_A)):
    A.append(float(temp_A[i] ) )
    

print len(A)

def prob(s, gc):
    p = float(gc) / 2.0
    q = float(1-gc) / 2.0
    return p ** s.count('G') * p ** s.count('C') * q ** s.count('A') * q ** s.count('T')

B = []
B_string = ''
for i in range(0, len(A)):
    B.append(np.log10(prob(s, A[i])  ) )
    B_string = B_string + ' ' + str(B[i])
    #print B_string
print B_string


    
