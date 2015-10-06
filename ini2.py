import sys

s = sys.argv[1]

L1 = int(sys.argv[2])
R1 = int(sys.argv[3])
L2 = int(sys.argv[4])
R2 = int(sys.argv[5])

t = s[L1:R1 + 1]
u = s[L2:R2 + 1]

print t, u