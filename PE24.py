import math, time
t = time.time()

#create dictionary of lexographic permutation 

def fact(a):
	answer = 1
	for i in range(1, a+1):
		answer *= i 
	return answer
	
#define lex

'''
def lex(n):
	p = [None]*fact(len(n))
	if len(n) == 2:
		n.sort()
		p[0] = n[:]
		n.reverse()
		p[1] = n[:] 
		return p
	else:
		count = 0
		for i in range(0, len(n)): #first number
			tbp = n[:]
			tbp.pop(i)
			for j in range(0, fact(len(tbp))):
				p[count] = [n[i]] + lex(tbp)[j]
				count += 1
				if count == 1000001:
					return p
		return p
'''

num = 1000000
L = [0,1,2,3,4,5,6,7,8,9]
Y = []

for i in range(9, 0, -1):
	print num
	print fact(i)
	a = num / fact(i)
	print a
	Y.append(L.pop(a))
	print L
	num = num % fact(i)
	if num == 0:
		for j in range(0,len(L)):
			Y.append(L[j])
print Y

'''
print lex([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[999999]
'''

'''
print len([1,2,3])
print fact(len([1,2,3]))
'''
print time.time() - t




