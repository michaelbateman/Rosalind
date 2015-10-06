
	    

filename = 'rosalind_motz.txt'
with open(filename,'r') as in_file:
	trash = in_file.readline()
	dna = ''
	for line in in_file:
		
		temp = line.strip()
		dna += temp
	
print dna

N = len(dna)

A = [[0 for j in range(0, N)] for i in range(0, N)]

for j in range(0, N):
	A[j][j] = 1
for j in range(0, N-1):
	
	if dna[j]+dna[j+1] in ['AU', 'UA', 'GC', 'CG']:
		A[j][j+1] = 2
	else:
		A[j][j+1] = 1

#print A 	
	
	
for l in range(2, N):
	for j in range(0, N):
	
		if j+l > N - 1:
			pass
		else:
			#print 'hello'
			i = j+l
#			print j, i
			total = 0 
			for k in range(j+1, i+1):
				if dna[j] + dna[k] in ['AU', 'UA', 'GC', 'CG']:
			#		print 'ehhleo'
					#total+= A[j+1][k-1] * A[k+1][i]
					
					if i - j + 1 == 2:  
						total += 1
					elif i - j + 1 == 3:
						total += 1
					elif i - j + 1 == 4 and k - j== 1:  
						total += A[i-1][i]
						#if j == 1 and i == 4:print 'one', A[i-1][i]
					elif i - j + 1 == 4 and k - j== 2:  
						total += 1
						#if j == 1 and i == 4:print 'two', 1
					elif i - j + 1 == 4 and k - j== 3:  
						total += A[j+1][j+2]
						#if j == 1 and i == 4:print 'three', A[j+1][j+2]
					
					elif k == i:
						total += A[j+1][k-1]
					elif k == i - 1:
						total += A[j+1][k-1]
					elif k == j+1 :
						total += A[k+1][i]
					elif k == j+2:
						total += A[k+1][i]
					else:
						total+= A[j+1][k-1] * A[k+1][i]
				#if j == 1 and i == 4:
					#print total
			A[j][i] = A[j+1][i] + total



#print ' N = ', N
print A[0][N-1] % 1000000

#print A[0][0]
#print A[0][1]
#print A[0][2]
#print A[0][3]

#print A