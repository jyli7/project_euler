import math, time
start = time.time()

#sieve method for getting list of primes.
def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0;m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2;s[j]=0
			while j<half:
				s[j]=0;j+=m
		i=i+1;m=2*i+3
	return [2]+[x for x in s if x]
 

# filter bad primes
goodNums=set(['1','3','7','9'])
good_filter=lambda x: not set(str(x)).difference(goodNums)
primes=filter(good_filter,primes(1000000))
 
def rotate(n_str):
    return n_str[-1]+n_str[:-1]
def isCircullar(n_str):
    global primes
    for i in range(len(n_str)-1):
        n_str=rotate(n_str)
        if not int(n_str) in primes:
            return 0
    return 1
 
circullarCounter=lambda x,y:x+isCircullar(str(y))
 
#explicitly include 2 and 5 to circullar primes (excluded at filtering procedure)
print reduce(circullarCounter,primes,2)

'''

print time.time() - start

