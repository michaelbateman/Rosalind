import numpy as np

n = 10000
B = []
for i in range(0,n):
	B.append(i*i % n)

A = np.sort(B)

for i in range(0,n):
	#print i
	start = i+1
	end = n-1
	a = A[i]
	temp = - a
	b = A[start]
	c = A[end]
	while start < end:
		#start = start + 1
		#start +=1
		#b = A[start]
		#c = A[end]
		if b + c < temp:
			start = start + 1
			b = A[start]		
		else:
			#start = start + 1
			end = end - 1
			c = A[end]
			
			
print 'hello'
			
		
		


