#Define the function
#Apply the function to numbers 1 - 999,999

# (1) 

import math, time
init_time = time.time()

def col(n):
	count = 1
	while n != 1:
		if n % 2 == 0:
			n = n / 2
			count += 1
		else:
			n = 3*n + 1
			count += 1
	return count 

# (2)

answer = 0
max = 0

for i in range(2, 1000000):
	if col(i) > max:
		max = col(i)
		answer = i

print answer

print time.time() - init_time
	
		