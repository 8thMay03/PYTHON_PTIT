import math

t = int(input())

while t>0:
    n, x, m = list(map(float,input().split()))
    x /= 100
    ans = math.log(m / n, 1 + x)
    if ans != int(ans):
        ans = int(ans) + 1
    print(ans)
    t -= 1
