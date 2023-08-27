import math

l, r = map(int, input().split())
for i in range(l, r-1):
    a = i
    for j in range(i+1, r):
        b = j
        if(math.gcd(a, b) == 1):
            b = j
            for k in range(j+1, r+1):
                c = k
                if math.gcd(b, c) == 1:
                    if math.gcd(a, c) == 1:
                        print('('+ str(a) + ', ' + str(b) + ', ' + str(c) + ')')