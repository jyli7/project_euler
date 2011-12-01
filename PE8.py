num = open('PE8_number.txt', 'r')

number = num.read()

print number
print len(number)

#Now that we have the number, in string form, 
#we can actually answer the question at hand

high = 1
sum = 0

for j in range(0, 955, 1):
	first = number[j]
	second = number[j+1]
	third = number[j+2]
	fourth = number[j+3]
	fifth = number[j+4]
	sum = int(first) * int(second) * int(third) * int(fourth) * int(fifth)
	if sum > high:
		high = sum

print high 	

