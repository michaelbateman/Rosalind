import sys

s = 'rosalind_ini5.txt'
try:
    input_file = open(s, "r")
    print "input file is", input_file.name
except IOError:
    print "Oh no, we couldn't open our file!"
    

print ' '
print ' '
print ' '
print ' '

i = 1
for line in input_file:
    if i % 2 == 0:
	print line.strip()
    else:
	pass
    i +=1
