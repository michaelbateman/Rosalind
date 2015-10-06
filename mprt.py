import sys
import urllib
#import requests

s = 'rosalind_mprt.txt'

try:
    input_file = open(s, "r")
    print "input file is", input_file.name
except IOError:
    print "Oh no, we couldn't open our file!"




def read_fasta(file_name):
	
	s = file_name

	try:
    		input_file = open(s, "r")
    		print "input file is", input_file.name
	except IOError:
	    	print "Oh no, we couldn't open our file!"
	

	sample_dict = {}
	temp = ''
	sample = ''
	
	for line in input_file:
	    if '>' in line:	
		temp = line.rstrip()
		sample = temp.lstrip('>')
		#print 'SAMPLE:  ', temp2
		my_dna = ''
    	else:
		my_dna = my_dna + line.strip()
		sample_dict.update({ sample: my_dna })
	
	
	return sample_dict
	
	
	
	
	
	

def find_motif(prot):
	sites = []
	for j in range(0, len(prot)):
		if j+ 3 >= len(prot):
			break
		if (prot[j] == 'N' and prot[j+1] != 'P' and prot[j+2] in ['S','T'] and prot[j+3] !='P'):
			sites.append(j)	
			
	return sites

def Nglyc(prot_id):
	link = 'http://www.uniprot.org/uniprot/' + prot_id +'.fasta'

	f = urllib.urlopen(link)
	myfile = f.read()
	#print myfile
	
	t = 'temp_out_file.txt'
	with(open(t, 'w')) as out_file:
		for a in myfile:
			out_file.write(a)
	

	try:
    		input_file = open(t, "r")
    		#print "input file is", input_file.name
	except IOError:
	    	print "Oh no, we couldn't open our file!"
		
	for line in input_file:
		if '>' in line:	
			temp = line.rstrip()
			sample = temp.lstrip('>')
			#print len(sample)
			my_prot = ''
	#		print line
    		else:
			my_prot = my_prot + line.strip()
		
	
	prot = my_prot
    
	    
	if len( find_motif(prot) ) > 0:
		print 
		print prot_id
		for j in find_motif(prot):
			print j+1,
    
    
    

for line in input_file:
	temp = line.strip()
	#print temp
	Nglyc(temp)
	

