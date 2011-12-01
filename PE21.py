import math, time
init_time = time.time()

#define funciton d(n)

def d(n):
	if n == 1:
		return 0
	cap = int(math.sqrt(n)) 
	if math.sqrt(n) - int(math.sqrt(n)) != 0: #if NOT a perfect squrae
		sum = 1
		for i in range(2, cap+1, 1):
			if n % i ==0:
				sum += (i + n/i)
	else: #if a perfect square
		sum = 1 + int(math.sqrt(n))
		for i in range(2, cap, 1):
			if n % i == 0:
				sum += (i + n/i)
	return sum 

print d(220)

#create dictionary with n:d(n) 

dict = {}
upbound = 10000
for i in range(1, upbound+1):
	dict[i] = d(i)

#go through dictionary to find amicable numbers

amlist = []

for i in range(2, upbound+1):
	if i == dict.get(dict.get(i)) and i != dict.get(i):  
		amlist.append(i)
		amlist.append(dict[i])

print amlist

totalsum = 0

for i in range(0, len(amlist)):
	totalsum += amlist[i]

print totalsum/2

print time.time() - init_time
