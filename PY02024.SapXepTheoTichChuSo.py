def MulDigit(a):
    s = 1
    while a > 0:
        s *= (a%10)
        a //= 10
    return s

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x: (MulDigit(x), x))
    for i in a:
        print(i, end = ' ')
    print()