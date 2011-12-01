import math, time
now = time.time()

t = ''

for i in range(1, 300000):
	t = t + str(i)

print t
print int(t[0])*int(t[9])*int(t[99])*int(t[999])*int(t[9999])*int(t[99999])*int(t[999999])





print time.time() - now

