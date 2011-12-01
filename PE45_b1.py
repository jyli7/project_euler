import math, time
from set import Set

now = time.time()
	
def pent(n):
	return n*(3*n-1)/2

def hex(n):
	return n*(2*n-1)

n = 166

h = Set([hex(x) for x in range(144, 100000)])

while 1:
	pent(n)
	if pent(n) in h:
		print pent(n)
		break
	n += 1

print time.time() - now

