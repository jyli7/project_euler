#create an empty array
#fill in the array with pascal's triangle like specifications  

import math, time

init_time = time.time()

a = 2**1000
b = str(a)

sum = 0

for i in range(0, len(b)):
	sum = sum + int(b[i])

print sum

print time.time() - init_time