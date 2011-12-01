import math, time
init_time = time.time()

mylist = [2, 3, 3, 1]
d = {}

'''
for x in mylist:
	d[x] = 1

print d
mylist = list(d.keys())

print mylist
'''

biglist = []

for i in range(2, 101):
	for j in range(2, 101):
		biglist.append(i**j)

d = {}
for x in biglist:
	d[x] = 1

biglist = list(d.keys())

print len(biglist)

print time.time() - init_time
