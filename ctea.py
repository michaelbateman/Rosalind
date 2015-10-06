
from rosalind_functions import *


filename = 'rosalind_ctea.txt'

my_dict = read_fasta(filename)

[dist, s, t, num] = num_min_aligns(my_dict[0],my_dict[1])




print
print
print
print


print dist
print s
print t
print num