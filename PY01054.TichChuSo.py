t = int(input())

while t>0:
    n = int(input())
    ans = 1
    while n>0:
        tmp = n % 10
        if tmp != 0:
            ans *= tmp
        n //= 10
    print(ans)
    t -= 1