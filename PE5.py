count = 0

for n in range(2520, 1000000000, 2520):
	for i in range(20,0,-1):
		if n % i != 0:
			count = 0
			break 
		count = count + 1
		if count > 5:
			print count
	if count == 20:
		break 

print n 