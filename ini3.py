import sys


a = int(sys.argv[1])
b = int(sys.argv[2])

total = 0

for x in range(a,b+1):
    if (x % 2 == 1):
        total += x
    else:
	pass
    
print total

