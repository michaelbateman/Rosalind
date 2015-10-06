
import sys



def cat(s):
    #print s
    if len(s) ==0:
	return 1
    if len(s)%2 == 1:
	print ' OOPs, there is a problem'
	return 0
    if len(s) == 2:
	#print s
	if s in ['AU', 'UA', 'GC', 'CG']:
	    return 1
	else:
	    return 0
    
    if s.count('A') != s.count('U'):
	return 0
    if s.count('G') != s.count('C'):
	return 0
	
	
    
    
    
    
    
	
	
    total = 0
    for j in range(1, len(s)):
	L = len(s)
	if j %2 == 1 and s[0]+s[j] in ['AU', 'UA', 'GC', 'CG']:
		if j < L/2:
			x = cat(s[1:j])
			if x > 0:
				y = cat(s[j+1:])
				temp = total + x*y
				total = temp % 1000000 # one million
		else:
			x = cat(s[j+1:])
			if x > 0:
				y = cat(s[1:j])
				temp = total + x*y
				total = temp % 1000000 # one million
    
    #for j in range(1, len(s)):
	#if j==3:
	    #if s[1]+s[2] in ['AU', 'UA', 'GC', 'CG'] and s[0]+s[3] in ['AU', 'UA', 'GC', 'CG']:
		#temp = total + cat(s[1:j]) * cat(s[j+1:])
		#total = temp % 1000000 # one million
	#elif j == len(s) - 3:
	     #if s[-1]+s[-2] in ['AU', 'UA', 'GC', 'CG']and s[0]+s[-3] in ['AU', 'UA', 'GC', 'CG']:
		#temp = total + cat(s[1:j]) * cat(s[j+1:])
		#total = temp % 1000000 # one million
	##print j
	#elif j %2 == 1 and s[0]+s[j] in ['AU', 'UA', 'GC', 'CG']:
	    ##print s[0]+s[j]
	    #temp = total + cat(s[1:j]) * cat(s[j+1:])
	    #total = temp % 1000000 # one million
	    ##print total
    #print total
    return total
	    

filename = 'rosalind_cat.txt'
with open(filename,'r') as in_file:
	trash = in_file.readline()
	dna = ''
	for line in in_file:
		
		temp = line.strip()
		dna += temp
	
print dna

cat_dict = {}


L = len(dna)

#for j in range(0, L):
	
	#cat_dict.update({(j,j):1})
	#cat_dict.update({(j,j+1):0})
	#cat_dict.update({(j,j+3):0})
	#if dna[j]+dna[j+1] in ['AU', 'UA', 'GC', 'CG']:
		#cat_dict.update({(j,j+2):1})
	#else:
		#cat_dict.update({(j,j+2):0})
l = 0
while l <= L:
	
	for j in range(0, L+1 - l):
		
		if l == 0:
			cat_dict.update({(j, j+l): 1})
		elif l ==2 and dna[j]+dna[j+1] in ['AU', 'UA', 'GC', 'CG']:
			cat_dict.update({(j, j+l): 1})
		elif l==2:
			cat_dict.update({(j, j+2): 0})
			
		elif l %2 ==1:
			cat_dict.update({(j, j+l): 0})
		else:
			total = 0
			temp = 0
			for i in range(1,l):
				if i %2 ==0: pass
				elif dna[j] + dna[j+i] not in ['AU', 'UA', 'GC', 'CG']:
					pass
				else:
					x = cat_dict[(j+1, j+i )]
					if i == l-1 and dna[j]+dna[j+i] in ['AU', 'UA', 'GC', 'CG']:
						y = 1
					elif i == l-1:
						y = 0
					else:
						y = cat_dict[(j+i+1, j+l)]
					temp = total + x*y
					total = temp % 1000000 # one million
				#	print j, l, i,x*y
			
			cat_dict.update({(j, j+l): total })
			#print cat_dict[(j, j+l)]
	l+=1
#print cat_dict
print dna

print cat_dict[(0,L)]


#print cat(dna)


