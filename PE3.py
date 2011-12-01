def isprime(x):
	i = 0
	for i in range(2, x/2 + 1, 1):
		if x % i == 0:
			return False 
			break
	if i == x/2:
		return True

y = 600851475143

for i in range(int(100000/2), 0, -1):
	if y % i == 0:
		if isprime(i) == True:
			print i
			break 


	
	