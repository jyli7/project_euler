import time, math

#FORM THE SPIRAL

n = 1 #current number
cx = 0 #current x
cy = 0 #current y

spiral = {(cx, cy): n}

t = 1 #counter for the current path length 

max = 1002001

while n < max:	
	for a in range(1, t+1): #move right; loop is number of spaces we move
		cx = cx + 1
		cy = cy + 0
		n = n + 1
		spiral[(cx, cy)] = n
		if n == max:
			break
			
	for a in range(1, t+1): #move down
		if n == max:
			break
		cx = cx + 0
		cy = cy - 1
		n = n + 1
		spiral[(cx, cy)] = n 
	
	t = t+1 #(add a space)
	
	for a in range(1, t+1): #move left
		if n == max:
			break
		cx = cx - 1
		cy = cy + 0
		n = n + 1
		spiral[(cx, cy)] = n 
		
	for a in range(1, t+1): #move up
		if n == max:
			break
		cx = cx + 0
		cy = cy + 1
		n = n + 1
		spiral[(cx, cy)] = n 
	
	t = t+1 #(add a space)

#ADD DIAGONAL LENGTHS WITHIN SPIRAL

answer = 0
diag = 0


#top to bottom 
i = -500
j = 500

while diag < 1001:
	answer += spiral[(i,j)]
	i += 1
	j -= 1
	diag += 1


#bottom to top
i = -500
j = -500

diag = 0

while diag < 1001:
	answer += spiral[(i,j)]
	i += 1
	j += 1
	diag += 1

print answer-1