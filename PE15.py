#create an empty array
#fill in the array with pascal's triangle like specifications  

import math, time

init_time = time.time()

#fill array with 0s 

ary = []
line = []

for i in range(1, 21):
	for j in range(1, 21):
		line.append('0')
	ary.append(line)
	line = []


#fill in the bottom row and rightmost row with 1s

for i in range(0,20): #fill rightmost column with 1s
		ary[i][19] = 1

for j in range(0,20): #fill bottom-most row with 1s
		ary[19][j] = 1

print ary	

#fill in the rest of the array 

i = 19
j = 19
count = 0

while count != 19:
	ary[i][j]

print time.time() - init_time