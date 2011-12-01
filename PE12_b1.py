#

import time, math
initialtime = time.time()

def nofactors2(num):
	count = 0
	x = math.sqrt(num)
	y = int(math.ceil(x))
	if x - y == 0:
		count = 1
	count += 2*len(filter(lambda a: num % a == 0, range(1,y)))
	return count




print "That took ", (time.time() - initialtime), " seconds"
	