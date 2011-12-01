import math, time
start = time.time()

def IsPrime(n): 
	if n == 2: 
		return 1 
	elif n % 2 == 0: 
		return 0 
	upper = int(math.sqrt(n) + 1)
	for i in range(3, upper, 1):
		if n % i == 0:
			return 0
	return 1

dnt = []
circ = [2, 3, 5, 7, 197, 971, 719]


for i in range(11, 1000000):
	if i not in dnt and i not in circ:
		if IsPrime(i) == 1:
			switch = 0
			s = str(i)
			t = ''
			sl = []
			for j in range(0, len(s)):
				t = s[j:]
				t = t + s[:j]
				sl.append(int(t))
			for x in sl:
				if IsPrime(x) == 0:
					dnt = dnt + sl
					switch = 1
					break
			if switch == 0:
				circ = circ + sl
				
circd = {}
for x in circ:
	circd[x] = 1

circ = list(circd.keys())
print len(circ)

print time.time() - start

