
import sys


s = sys.argv[1]

M = max(s.count('G'), s.count('C'))
N = max(s.count('A'), s.count('U'))

k = min(s.count('G'), s.count('C'))
j = min(s.count('A'), s.count('U'))


prod = 1

for i in range(0, k):
	prod = prod*(M-i)
	print ' i = ', i
	print prod
x = prod

prod = 1
print 
print

for i in range(0, j):
	prod = prod*(N-i)
	print ' i = ', i
	print prod
y = prod

print 'M = ', M
print 'N = ', N
print 'k = ', k
print 'j = ', j



print x
print y
print 
print

print x*y