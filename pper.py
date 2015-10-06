#Given: Positive integers n and k such that 100>=n>0 and 10>=k>0.

#Return: The total number of partial permutations P(n,k), modulo 1,000,000.

import sys
import scipy.misc

n = int(sys.argv[1])
k = int(sys.argv[2])

product = 1

for j in range(0, k):
    temp = product * (n - j)
    product = temp % 1000000 # modulo one million
    
print product