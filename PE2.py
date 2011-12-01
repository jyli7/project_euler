a = 1
b = 2
sum = 0
print a

while b < 4000000:
	if b % 2 == 0:
		sum = sum + b
	old_b = b 
	b = b + a
	a = old_b
	
print sum 
	



	
	
	
		
	
		
	
	
