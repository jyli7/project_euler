def problem6(r): 
	return sum(r)** 2- sum([x** 2 for x in r]) 

print problem6(range(1,101)) 
