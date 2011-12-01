import math, time
from decimal import *
now = time.time()

print 1.0/3
print Decimal(1)/Decimal(983)

#See if the decimal repeats
#If so, measure the decimal's recurring cycle 
'''
outermax = 0
count = 0
answer = 0

for i in range(1,1001):
	a = Decimal(1.0)/Decimal(i)
	s = str(a)
	innermax = 0
	if len(s) > 8:
		for j in range(2, 10):
			for k in range(1, 16):
				if s[j:(j+k)] == s[(j+k):(j+2*k)] and s[(j+k):(j+2*k)] == s[(j+2*k):(j+3*k)]:
					innermax = k
					count = 1
					break
			if count == 1:
				count = 0
				break
		if innermax > outermax:
			outermax = innermax
			answer = i
	
print outermax, answer
'''				
print time.time() - now

