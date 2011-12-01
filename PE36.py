import math, time
init_time = time.time()

#create function to convert bases
#create function to find palindromes 

def bt(n):
	s = ''
	while n != 1:
		r = n%2 #get remainder
		s = s + str(r) #concatenate
		n = n/2 #get next number
	return '1' + s[::-1] 	

def rbt(s):
	count = 0
	sum = 0
	for y in range(len(s)-1, -1,-1):
		sum += int(s[y])*2**count
		count += 1
	return sum
	

print rbt('100101')

print bt(2)

def palin(s):
	if len(s) == 1:
		return True
	for i in range(0, len(s)/2):
		if s[i] != s[(-i-1)]:
			return False
	return True

print palin('5845'), palin(bt(585))

sum = 0

for a in range(1, 1000000):
	if palin(str(a)) == True and palin(bt(a)) == True:
		print a
		print bt(a)
		sum += a

print sum

print time.time() - init_time
