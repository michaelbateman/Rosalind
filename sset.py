import sys

n = int(sys.argv[1])

prod = 1
for i in range(0, n):
	temp = prod * 2
	prod = temp % 1000000 # modulo one million
	
print prod