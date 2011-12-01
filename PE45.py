import math, time
now = time.time()

def triag(n):
	return n*(n+1)/2
	
def pent(n):
	return n*(3*n-1)/2

def hex(n):
	return n*(2*n-1)
	
t = []
p = []
h = []

for i in range(140, 400000):
	t.append(triag(i))
	p.append(pent(i))
	h.append(hex(i))

def intersect(a, b, c):
	return list(set(a) & set(b) & set(c))

print intersect(t, p, h)


'''
for j in range(40756, 1000000):
	if j in t and j in p and j in h:
		print j 
		break
'''

print time.time() - now

