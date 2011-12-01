#take in each line, one at a time 
#convert each line to an int 

import math, time

init_time = time.time()

a = open('PE13_number.txt', 'r')
input = a.read()

lines = input.split('\n') 


sum = 0

for i in range(0, 100):
	num = long(lines[i])
	sum = sum + num

fullanswer = str(sum)
realanswer = fullanswer[0:10]

print realanswer

print time.time() - init_time