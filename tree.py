#Given: A positive integer n (n<=1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

#Return: The minimum number of edges that can be added to the graph to produce a tree.


import numpy as np






s = 'rosalind_tree.txt'

try:
    input_file = open(s, "r")
    print "input file is", input_file.name
except IOError:
    print "Oh no, we couldn't open our file!"

e = 0
ctr = 0

for line in input_file:
    ctr +=1
    temp = line.strip()
    temp2 = temp.split()
    if len(temp2) == 1:
	n = int(temp2[0])
	print ' n = ', n
	
    else:
	e+=1
	
print 'n = ', n 
print 'e = ', e
print 'ctr = ', ctr

print 'Answer is ', n - 1 - e