import time, math

def spire(num):
    sum = 1
    top = num*num
    for i in range(num-1, 1, -2):
            for j in range(4):
                    sum += top
                    top -= i
    return sum

print spire(5)
