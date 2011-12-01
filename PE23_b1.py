import math, time
init_time = time.time()

def abun(N):
    Q = dict.fromkeys(range(1,N+1), 0) 
    for q in Q:
        for k in [q*n for n in range(1,N/q+1) ]:
            if q!=k: Q[k] += q
    return [ q  for q in Q if Q[q]>q]
 
N = 20161; A = abun(N); possible = set() 
for a in A:
    for b in A:
        if a+b < N: possible.add( a+b )
        else: break
 
print sum([p for p in range(N) if p not in possible])


print time.time() - init_time
