def find(k, A):
        bot =0
        top = len(A)
        ctr = 0
        while bot < top and ctr < 100:
                ctr +=1
                mid = (bot + top)  / 2
        #       print ' k = ' , k
        #       print ' A[mid] = ', A[mid]
                if A[mid] == k: return mid +1
                elif A[mid]< k: bot = mid
                elif A[mid] > k: top = mid
        return -1


import sys

s = 'rosalind_bins.txt'
input_file = open(s, 'r')

lines = input_file.readlines()


temp = lines[2].strip()
A = temp.split()

temp2 = lines[3]
temp3 = temp2.strip()
B = temp3.split()

#print A
#print B

#find(10, A)

for i in range(0, len(A)):
        A[i] = int(A[i])
#print A
#find(10,A)
#print
#print
for i in range(0, len(B)):
        B[i] = int(B[i])
        print find(B[i], A),