import math, time
init_time = time.time()

#let's try making the fib sequence with lists, to see if the computer can easily store long sequences of numbers 

seq = [1, 1, 1]


for i in range(3, 100000):
	seq.append(seq[i-1]+seq[i-2])
	length = len(str(seq[i]))
	if length == 1000:
		print i
		break 

print time.time() - init_time