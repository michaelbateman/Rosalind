#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.





s = 'rosalind_gc.txt'

try:
    input_file = open(s, "r")
    print "input file is", input_file.name
except IOError:
    print "Oh no, we couldn't open our file!"




def gc( dna ):
    weight = {'A': 0, 'T': 0, 'C':1, 'G': 1} 
    total = 0 
    for base in dna:
	total = total + weight[base]
    #print total
    #print len(dna)
    #return 0
    if len(dna) == 0:
	return 0
    else:
	return (100.0 *   float(total) / float(len(dna))  )
	


gc_dict = {}
temp = ''
temp2 = ''

for line in input_file:
    if '>' in line:
	
	
	temp = line.rstrip()
	temp2 = temp.lstrip('>')
	#print 'SAMPLE:  ', temp2
	my_dna = ''
    else:
	my_dna = my_dna + line.strip()
	gc_dict.update({ temp2: gc(my_dna) })
	



for sample in gc_dict:
    print sample, gc_dict[sample]
    


    
print ''
print ''
print ''

M = max(gc_dict.values())

for sample in gc_dict:
    if abs(gc_dict[sample] - M) <= .001:
	print sample
	print M

    






