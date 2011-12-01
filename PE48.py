import math, time
init_time = time.time()

total = 0

for i in range(1, 1001):
	total += i**i

answer = str(total)
print answer[-10:]


print time.time() - init_time
