# (1) create divnum function 
# (2) apply divnum function to a 'for' loop that lists out 
# the triangle numbers

import time, math

s = time.time()

#(1)
def divnum(n):
	if n == 1: 
		return 1
	if int(math.sqrt(n))**2 == n:
		answer = 3 # for 1, n, and the sqrt
	else:
		answer = 2 # for 1 and n
	upperbound = int(math.ceil(math.sqrt(n)))  
	for i in range(2, upperbound, 1):
		if n % i == 0:
			answer += 2 # +2 b/c you have the lower factor and the higher factor	
	return answer 

#testing the divnum function.
'''
print divnum(1)
print divnum(6)
print divnum(8)
print divnum(15)
print divnum(21)
print divnum(28)
print divnum(36)
'''

#(2) 

nextnum = 2
testnum = 1
count = 0

while count < 501:
	testnum = testnum + nextnum
	count = divnum(testnum)
	nextnum += 1

print testnum
print "That took ", (time.time() - s), " seconds"
	