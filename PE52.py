def breakup(n):
	L = []
	for x in str(n):
		L.append(x)
	return L

#create function that tells you if *2 has same digits
#This requires a three step loop:
	#Go through each number 
	#Multiply by 2-6
	#For each product, cycle through the digits 

num = 10
count = 0
trigger = 0


while trigger == 0:
	brokenum = breakup(num)
	subtally = 0
	for j in range(2,7):
		prod = num*j
		brokeprod = breakup(prod)
		count = 0 #count is used to count within the third loop, when cycling through digits 
		for i in range(0, len(brokenum)):
			if brokenum[i] in brokeprod:
				brokeprod.remove(brokenum[i])
				count += 1
				if count == len(brokenum): #third loop worked!
					subtally += 1
					break
			else:
				subtally = 0
				break
		if subtally == 5: #second loop worked!
			trigger = 1
			print num
			break 
		elif subtally == 0:
			break
		else:
			continue
	num += 1


			
		
				