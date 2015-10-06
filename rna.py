import sys

print ''
print ''
print ''
print ''

dna = sys.argv[1]

rna = ''

for x in dna:
    if x == 'T':
        rna = rna + 'U'
    else:
        rna = rna + x
    


print rna
