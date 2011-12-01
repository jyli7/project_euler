import time, math 
s = time.time() 

def IsPrime(n): 
	if n == 2: 
		return 1 
	elif n % 2 == 0: 
		return 0 
	upper = int(math.sqrt(n) + 1)
	for i in range(3, upper, 1):
		if n % i == 0:
			return 0
	return 1

sum = 2
for i in range(3,2000001,2):
	if IsPrime(i) == 1:
		sum += i

print sum
print "That took %d seconds!" % time.time()-s