import sys

s = 'rosalind_ini6.txt'
try:
    input_file = open(s, "r")
    print "input file is", input_file.name
except IOError:
    print "Oh no, we couldn't open our file!"
    
for line in s:
    temp = line.strip()
    my_list = temp.split()

print ''
print ''
print ''
print ''


string = sys.argv[1]

dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
print dict

print string

for x in string:
    dict[x] += 1
    


print dict['A'], dict['C'], dict['G'], dict['T'] 