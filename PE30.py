import math, time
t = time.time()

p = 5
answer = 0

for i in range(1000, 1000000):
	sum = 0
	for a in str(i):
		sum += (int(a))**p
	if sum == i:
		answer += i

print answer

print time.time() - t

