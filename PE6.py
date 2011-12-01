sumsquare = 0
squaresum = 0
sum_1 = 0
sum_2 = 0

for i in range(1, 101):
	sum_1 = i + sum_1
squaresum = sum_1**2

for i in range(1, 101):
	sum_2 = i**2 + sum_2
sumsquare = sum_2

answer = squaresum - sumsquare 
print answer