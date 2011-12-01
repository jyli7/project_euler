import math, time
now = time.time()

def triag(n):
	return n*(n+1)/2
	
tlist = []

for i in range(1, 200):
	tlist.append(triag(i))

alpha = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

thefile = open('words.txt', 'r')
words = thefile.read()[1:-1]
wordlist = words.split('","')

count = 0

for x in wordlist:
	sum = 0
	for i in x:
		sum += int(alpha[i])
	if sum in tlist:
		count += 1

print count


print time.time() - now

