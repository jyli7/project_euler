def nway( total, coins):
    if not coins:
        print "ONE", "total=", total, "NO MORE COINS!"
        return 0
    c, coins = coins[0], coins[1:]
    count = 0 
    if total % c == 0:
        count += 1
        print "count increased"
    print "TWO", "total=", total, "c=", c, "count=", count
    for amount in xrange( 0, total, c):
        count += nway(total - amount, coins)
        print "THREE", "total=", total, "c=", c, "CYCLED!", "count=", count
    print "FOUR",  "total=", total, "RETURNED!", count
    return count
# main

print nway(10, (1,2,5, 10))









'''
D = {1:[1],
     2:[[2], [1, 1]],
     3:[[2, 1], [1, 1, 1]]}


def create_list(x):
    for coin in coins:
        list = []
        if x>coin:
            div = x / coin
            remainder = x % coin
            for i in range(0, div+1):
                if i == div:
                    if remainder >0:
                        list.append(remainder)
                    else:
                        break
                else:
                    list.append(coin)
            return list

def combo(y):
    l = [] #mini-lists that will be merged together to form the big list
    L = []
    length = len(y)
    count = 0
    for i in range(0, length):
        if i == 0:
            l_1 =D[y[i]]
        if i == 1:
            l_2 =D[y[i]]
        if i == 2:
            l_3 =D[y[i]]
        if i == 3:
            l_4 =D[y[i]]
        count += 1
    if count == 2:
        L = [[a, b] for a in l_1 for b in l_2]
    if count == 3:
        L = [[a, b, c] for a in l_1 for b in l_2 for c in l_3]
    if count == 4:
        L = [[a, b, c, d] for a in l_1 for b in l_2 for c in l_3 for d in l_4]
    for list in L:
        list.sort()
    if L:
        L.sort()
        last = L[-1]
        for i in range(len(L)-2, -1, -1):
            if last == L[i]:
                del L[i]
            else:
                last = L[i]
    return L


for a in range(4, 51):
    temp_1 = create_list(a)
    if a in coins:
        D[a] = [[a]] +combo(temp_1)
    else:
        D[a] = combo(temp_1)

D[100] = combo(create_list(100))
'''
 
