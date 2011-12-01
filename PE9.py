import math 

for a in range(1,400):
	if (500000 - 1000*a) % (1000 - a) == 0: 	
		b = (500000 - 1000*a) / (1000 - a) 
		c = math.sqrt(a**2 + b**2)
		print a, b, c
		print a*b*c
		
