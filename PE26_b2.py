import math, time
from decimal import *
now = time.time()

import itertools

'''
def recur_len(n):
    # digits for unit fraction 1/n
    r = 10 # initial remainder (10/n)/10
    seen = {} # remainder -> first pos
    for i in itertools.count(0):
        if r == 0:
            return 0  # divides evenly.
        elif r in seen:
            return i-seen[r] # curpos - firstpos
        seen[r] = i
        r= 10*(r % n)
 
len,i = max((recur_len(i),i) for i in range(2,1000))
print i
'''

print itertools.count(10)

print time.time() - now

