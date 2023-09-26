for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    mx = a[0]
    idx = 0
    for i in range(n):
        if a[i] > mx:
            mx = a[i]
            idx = i
    a.insert(idx, m)
    for i in a:
        if i < 0:
            print(i, end=' ')
    for i in a:
        if i >= 0:
            print(i, end=' ')
    print()