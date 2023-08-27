t = int(input())

while t>0:
    n, d = input().split()
    n, d = int(n), int(d)
    a = list(map(int,input().split()))
    for i in range (d,n):
        print(a[i], end = ' ')
    for i in range(0,d):
        print(a[i], end = ' ')
    print()
    t -= 1