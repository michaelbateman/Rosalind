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

my_list = string.split()
dict = {}

for x in my_list:
    if x in dict:
	dict[x] += 1
    else:
	dict[x] = 1


for word in dict.keys():
    print word, dict[word]