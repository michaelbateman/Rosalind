
import sys


temp = sys.argv[1]


temp2 = temp.strip()


bases = temp2.split()

bases.insert(0, ' ')
#print bases
L = ['']

for i in range(0, int(sys.argv[2]) ):
    temp = []
    for w in L:
	for a in bases:
	    temp.append(w+a)
    L = temp
    
for w in L:
	#print len(w)
	if w[0] != ' ':
		if w[1] != ' ' or (w[1] == ' ' and w[2] == ' '):
			print w