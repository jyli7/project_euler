import math, time
init_time = time.time()

file = open('names.txt', 'r')
temp = file.read()
names = temp.split(",")

for i in range(0, len(names)):
	names[i] = names[i][1:-1]

names.sort()

letters = {
'A':1, 
'B':2, 
'C':3, 
'D':4, 
'E':5, 
'F':6, 
'G':7,
'H':8,
'I':9,
'J':10,
'K':11,
'L':12,
'M':13,
'N':14,
'O':15,
'P':16,
'Q':17,
'R':18,
'S':19,
'T':20,
'U':21,
'V':22,
'W':23,
'X':24,
'Y':25,
'Z':26
}

def letscore(n):
	score = 0
	for i in range(0, len(n)):
		score += letters[n[i]]
	return score

total = 0
indiv = 0

for i in range(0, len(names)):
	indiv = (i+1) * letscore(names[i])
	total += indiv

print total

print time.time() - init_time
