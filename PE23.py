import math, time
init_time = time.time()

# 1 create a proper divisors function
# 2 create a list of abundant numbers below 28123
# 3 create a greater list of all the sums of those abundant numbers
#create a final list of numbers that aren't in that greater list 
#sum the numbers in that final list


def pdsum(n): #1 a function for the sum of the proper divisors
	sum = 0
	for i in range(1, int(math.sqrt(n))+1):
		if n % i == 0:
			sum += i + n/i
	sum -= n
	if math.sqrt(n) - int(math.sqrt(n)) == 0:
		sum -= int(math.sqrt(n))
	return sum

ab = [] #2 create a list of abundant numbers below 28123

top = 28125

for i in range(12, top):
	if pdsum(i) > i:
		ab.append(i)


gl = [] #3 create a greater list of the sums of the abundant numbers, without repeats

for i in range(0, len(ab)):
	count = 0
	total = 0
	if ab[i] + ab[i] < top:
		while total < top:
			total = ab[i] + ab[i+count] 
			gl.append(total)
			count += 1

#remove duplicates in gl 

dgl = {}
for x in gl:
	dgl[x] = 1

gl = list(dgl.keys())


#add up the numbers not in gl

sum = 0

for j in range(1, top):
	if j not in gl:
		sum += j

print sum

print time.time() - init_time
