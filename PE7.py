import time, math

s = time.time()

def isprime(x):
	upperbound = int(math.sqrt(x)) + 1
	for i in range(2, upperbound):
		if x != 2 and (x % i == 0 or x % 2 == 0):
			return False
	return True

def IsPrime(x):
	if x == 2:
		return 1
	elif x % 2 == 0:
		return 0 
	upperbound = int(math.sqrt(x)) + 1
	for i in range(3, upperbound):
		if x % i == 0:
			return 0
	return 1 

count = 1
y = 3

while count < 10001:
	if IsPrime(y) == True:
		count += 1
	y += 2
	
print y 
print time.time() - s
	