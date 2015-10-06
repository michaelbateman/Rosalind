import sys


print ''
print ''
print ''
print ''


string = sys.argv[1]
sub = sys.argv[2]

L = len(sub)

locations = []

for i in range(0, len(string) + 1 - L):
    temp = string[i:i+L]
    if temp == sub:
	locations.append(i)
    else:
	pass
	
ans = ''
for i in range(0, len(locations)):
    ans = ans +  str(1 + locations[i]) + ' '

print ans