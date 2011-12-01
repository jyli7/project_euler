# (1) Take in grid as a list of lists 
# (2) Run a 'for' loop through the grid, starting at top left 

num = open('PE11_number.txt', 'r')

count = 1
grid = []
bg = []

# (1)

while count <21:
	line = num.readline()
	upperbound = len(line)
	for i in range(0, upperbound, 3):
		new = int(line[i:i+2])
		grid.append(new)
	bg.append(grid)
	count += 1
	grid = []

# (2)

# i are rows
# j are columns 

max = 0

for i in range(0, 17, 1): #most of the numbers
	for j in range(0, 17, 1): 
		prodright = bg[i][j] * bg[i][j+1] * bg[i][j+2] * bg[i][j+3]
		proddown = bg[i][j] * bg[i+1][j] * bg[i+2][j] * bg[i+3][j]
		proddiag = bg[i][j] * bg[i+1][j+1] * bg[i+2][j+2] * bg[i+3][j+3]
		if prodright > max:
			max = prodright
		if proddown > max:
			max = proddown			
		if proddiag > max:
			max = proddiag
	
for i in range(17,20,1): #for the numbers in the bottom three rows
	for j in range(0, 17, 1):
		prodright = bg[i][j] * bg[i][j+1] * bg[i][j+2] * bg[i][j+3]
		if prodright > max:
			max = prodright

for i in range(0,17,1): #for the numbers in the right three columns
	for j in range(17, 20, 1):
		proddown = bg[i][j] * bg[i+1][j] * bg[i+2][j] * bg[i+3][j]
		if proddown > max:
			max = proddown

for i in range(3,20,1): #for the bl to tr diag
	for j in range(0, 17, 1):
		proddiagup = bg[i][j] * bg[i-1][j+1] * bg[i-2][j+2] * bg[i-3][j+3]
		if proddiagup > max:
			max = proddiagup

print max
