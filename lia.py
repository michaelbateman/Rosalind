#Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

#Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.


import sys
import scipy.misc
k = int(sys.argv[1])
N = int(sys.argv[2])

total = 0 

x = 2**k



for j in range(N, x + 1):
    total += .25 ** j *.75 **(x - j) * scipy.misc.comb(x , j)
    
print total