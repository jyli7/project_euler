#Cycle through the potential numbers, from largest (1MM) to smallest (10,000) 
#For each of those numbers, check to see 
	#(1) Check to see if the number is a palindrome. If yes, then:
	#(2) Check to see if it's a product of two 3-digit numbers
	

switch = 0

for i in range(999999,100000,-1):
	s = str(i)
	if s[0] == s[-1] and s[1] == s[-2] and s[2] == s[-3] and switch == 0:
		for j in range(999, 100, -1):
			if i % j == 0:
				t = str(i/j)
				if len(t) == 3:
					print(i)
					switch = 1 
					break
	
