import math, time
t = time.time()

def fact(a):
	answer = 1
	for i in range(1, a+1):
		answer *= i 
	return answer
	
print 3*fact(9)

print 1000000 - 2*fact(9)
print fact(8)

L = [2]
num = 274240

for i in range(8, 1, -1):
	L.append(num / fact(i))
	num = num % fact(i) 

print L


print time.time() - t




