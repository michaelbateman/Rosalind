import time
import sys


length = int(sys.argv[1])

filename = 'rosalind_rear.txt'



def make_perm_dictionary(length):  # returns a list of permutations of length length
					# together with a map to an integer
			
	n = length
	my_perms = []
	new = []
	L = [[1]]
	for m in range(2, n + 1):
		temp = []
		for w in L:
			#print w
			for i in range(0, m):
				#print w
				#w.insert(i, m)
				#print w[0:i] + [m] + w[i:]
				
				#help = w[0:i] + [m] + w[i:]
				temp.append(w[0:i] + [m] + w[i:])
				#temp.append(tuple(w[0:i] + [m] + w[i:]))
				#print ' now', temp
				
				#w.remove(m)
				#print w
				#print temp
			#print 'temp', temp
		L = temp


	my_dict = {}
	ctr = 0
	for x in L:
		my_dict.update({ctr:x})
		ctr +=1

	return my_dict





with open(filename, 'r') as input_file:
	ctr = 0
	for line in input_file:
		#print ctr
		temp = line.strip()
		if ctr % 3 == 0:
			M = temp.split()
		elif ctr % 3 == 1:
			L = temp.split()
			#print R(M, 3, 1)
			#print ctr
	#		print rev_dist(tuple(M),tuple(L))
			print 'hi'
			#print testing(M,L)
			print 'bye'
		else:
			pass
		ctr +=1	







start = time.clock()
print len(make_perm_dictionary(length))
end = time.clock()
print end - start



trial_dict = {}


start = time.clock()

for j in range(0, 3000000):
	for x in range(0, 1):
		trial_dict.update({j:j + x})
	
end = time.clock()
print end - start
	






















sys.exit()




def reverse(A):
	return A[::-1]

def R(M, l, j):
	#M[j:j+l] = reverse(M[j:j+l])
	#return M
	#print M[0:j]
	#print M[j:j+l]
	#temp = M[j:j+l]
	#print temp
	#print reverse(temp)
	#print reverse(M[j:j+l])
	#print M[j+l:]
	#return M
	#return M[0:j] + M[j: j+l] + M[j+l:]
	return M[0:j] + reverse(M[j: j+l]) + M[j+l:]

def list_rev(M):
	M = list(M)
	ans = set()
	for l in range(2, len(M) + 1):
		for j in range(0, len(M)+1 - l):
			#print R(M,l,j)
			M[j:j+l] = reverse(M[j:j+l])
			ans.add(tuple(M))
			ans.add(tuple(R(M,l,j)))
			#print l, j
	return ans
			
def rev_dist(A,B):
	my_length = 0
	#if A == B:
	#	return 0
	my_list = set([A])
	already_done = set()
	while my_length < length:
		temp = set()
		for x in my_list:
			#print x
			if x == B:
				print 'We won'
				return my_length 
			elif x in already_done:
				#print 'already done', length
				pass
			else:
				#print 'trying next', length
				#temp_list = list_rev(x)
				#for t in temp_list:
				#	temp.add(t)
				temp.update(list_rev(x))
				already_done.add(x)
		my_list = temp
		#print 'length = ', my_length
		my_length +=1	
		
	return 10
		
		

		
def make_dict():
	n = length
	my_perms = []
	new = []
	L = [[1]]
	for m in range(2, n + 1):
		temp = []
		for w in L:
			#print w
			for i in range(0, m):
				#print w
				#w.insert(i, m)
				#print w[0:i] + [m] + w[i:]
				
				#help = w[0:i] + [m] + w[i:]
				temp.append(w[0:i] + [m] + w[i:])
				#temp.append(tuple(w[0:i] + [m] + w[i:]))
				#print ' now', temp
				
				#w.remove(m)
				#print w
				#print temp
			#print 'temp', temp
		L = temp
		#print L
	for w in L:
		#print w
		a = 2
	for j in range(1, 11):
		for i in range(1,11):
			a = 2
	my_dict = {}
	print
	print 'done'
	return L
	
def counting():
	for i in range(0, 1000000):
		if i %1000 ==0: print i
	return 0


def testing(A,B):
	j = 0 
	while (j < length):
		if B == A[:j] + reverse(A[j:]):
			#print j
			return j
		else:
			ind = A.index(B[j])
			A = reverse(A[:ind +1]) + A[ind+1:]
			j+=1	
			

old_perms = make_dict()
perms = set()
for x in old_perms:
	perms.add(tuple(x))
rev_dict = {}
my_index = {}
index = 0
for x in perms:
	if index % 100000 == 0: print index
	my_index.update({x:index})
	index +=1
	
	#y = list_rev(tuple(x))
	##rev_dict.update({tuple(x):list_rev(tuple(x))})

print
print 'index made'
print

for x in perms:
	if my_index[x] % 100000 == 0: print my_index[x]; print ''
	#y = list_rev(tuple(x))
	y = list_rev(x)
	temp = set()
	for elt in y:
		temp.add(my_index[elt])
	rev_dict.update({my_index[x]: temp})


with open(filename, 'r') as input_file:
	ctr = 0
	for line in input_file:
		#print ctr
		temp = line.strip()
		if ctr % 3 == 0:
			M = temp.split()
		elif ctr % 3 == 1:
			L = temp.split()
			#print R(M, 3, 1)
			#print ctr
			print rev_dist(tuple(M),tuple(L))
			print 'hi'
			#print testing(M,L)
			print 'bye'
		else:
			pass
		ctr +=1	

#print M
#list_rev(M)
#print list_rev(M)


