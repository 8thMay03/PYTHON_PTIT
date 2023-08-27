import math

t = int(input())

while t > 0:
    s = input()
    ss = s[::-1]
    if math.gcd(int(ss),int(s)) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1