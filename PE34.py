import math, time
init_time = time.time()


def fact(a):
	answer = 1
	for i in range(1, a+1):
		answer *= i 
	return answer


for i in range(0,1000):
	value = 0
	for x in str(i):
		value += fact(int(x))
	if value == i:
		print i 

print 145+40585



print time.time() - init_time
