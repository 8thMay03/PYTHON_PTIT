import math

c = ['A','B','C','D','E','F']

for _ in range(int(input())):
    n = int(input())
    s = input()
    if n==2:
        print(s)
        continue
    n = int(math.log(n,2))
    while len(s)%n != 0:
        s = '0' + s
    ans = ""
    while len(s) >= n:
        x = s[len(s)-n:]
        s = s[:-n]
        tmp = 0
        for i in range(n):
            tmp += int(x[i])*(2**(n-i-1))
        if tmp >= 10:
            tmp = c[tmp-10]
        ans = str(tmp) + ans
    print(ans)