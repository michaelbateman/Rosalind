import sys

print ''
print ''
print ''
print ''

dna = sys.argv[1]

rev_comp = ''

comp = { 'A': 'T', 'T':'A', 'C':'G', 'G':'C'}

L = len(dna)
i = 1

while i <= L:
    rev_comp = rev_comp + comp[dna[-i]]
    i +=1


print rev_comp
