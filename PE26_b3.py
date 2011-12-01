import math, time
from decimal import *
now = time.time()

def cycle(n): 
	myList = [1] 
	t = 1 
	f = (10**t) % n 
	while myList.count(f) == 0: 
		myList.append(f) 
		t = t + 1 
		f = (10**t) % n 
	try: 
		s = myList.index(f) 
	except ValueError: 
		s = 0 
		return t-s 

def solve(): 
	mx, val = 0, 0 
	for n in range(2, 1000): 
		m = cycle(n) 
		if m > mx: 
			mx = m 
			val = n 
	print(mx, val)

solve() 

print time.time() - now

