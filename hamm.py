

def hamming(a,b):
    if len(a) != len(b):
	return 'The two strings must have the same length!!!'
	
    else:
	dist = 0
	for i in range(0, len(a)):
	    if a[i] != b[i]:
		dist +=1
	    else:
		pass
        return dist



import sys

s = sys.argv[1]
t = sys.argv[2]

print hamming(s,t)