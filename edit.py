def read_fasta(file_name):
	
	s = file_name

	try:
    		input_file = open(s, "r")
    	#	print "input file is", input_file.name
	except IOError:
	    	print "Oh no, we couldn't open our file!"
	

	sample_dict = {}
	temp = ''
	sample = ''
	ctr = 0 
	for line in input_file:
	    if '>' in line:	
		ctr +=1
	#	print ctr
		temp = line.rstrip()
		sample = temp.lstrip('>')
		#print 'SAMPLE:  ', temp2
		my_dna = ''
	    else:
		my_dna = my_dna + line.strip()
		sample_dict.update({ ctr: my_dna })
	#	print my_dna
	
	
	return sample_dict
	
	
def edit_distance(s,t):
	M = len(s)
	N = len(t)
	A = [[0 for j in range(0, N+1)] for i in range(0, M+1)]
	
	for i in range(0, M+1):
		A[i][0] = i
	
	for j in range(0, N+1):
		A[0][j] = j
	
	for i in range(1, M+1):
		for j in range(1, N+1):
			a = A[i-1][j] +1
			b = A[i][j-1] +1
			if s[i-1] == t[j-1]:
				c = A[i-1][j-1]
			else:
				c = A[i-1][j-1] + 1
			A[i][j] = min(a,b,c)
	#print A
	return A[M][N]

filename = 'rosalind_edit.txt'

my_dict = read_fasta(filename)
#print my_dict[1]
#print my_dict[2]

print edit_distance(my_dict[1],my_dict[2])