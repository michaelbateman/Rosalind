
import sys


s = sys.argv[1]

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
    
    total = 0
    for j in range(1, len(s)):
	if j %2 == 1:
	    temp = total + cat(s[1:j]) * cat(s[j+1:])
	    total = temp % 1000000 # one million
    #print total
    return total
	    
	    
print cat(s)


