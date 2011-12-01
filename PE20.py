#create an empty array
#fill in the array with pascal's triangle like specifications  

import math, time

init_time = time.time()

def fact(n):
	factorial = 1
	for i in range(n, 0, -1):
		factorial = factorial * i
	return factorial 

longnum = fact(100)
longstr = str(longnum)
lenstr = len(longstr)

answer = 0
for j in range(0, lenstr):
	answer = answer + int(longstr[j])

print answer
print time.time() - init_time