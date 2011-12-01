c=0 
while True: 
	for b in range(0,c): 
		for a in range(0,b): 
			if a**2 + b**2 == c**2: 
				if a+b+c == 1000: 
					print "a=%d, b=%d, c=%d a*b*c=%d" % (a,b,c,a*b*c) 
	c+=1 