import sys

print ''
print ''
print ''
print ''

n = int(sys.argv[1])
k = int(sys.argv[2])

f = [1, 1]

for i in range(2, n + 1):
    f.append(f[i-1] + k * f[i-2])

print f
print f[n-1]


