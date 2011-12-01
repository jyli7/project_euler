#create an empty array
#fill in the array with pascal's triangle like specifications  

import math, time

init_time = time.time()

#Create pascal's triangle

row = [1, 1]
nextrow = [1]

count = 2

while count != 41:
	for i in range(1, len(row)): 
		nextrow.append(row[i-1] + row[i])
	nextrow.append(1)	
	row = nextrow
	nextrow = [1]
	count += 1

answer = row[len(row)//2]

print row
print answer


print time.time() - init_time