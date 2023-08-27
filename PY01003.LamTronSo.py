for _ in range(int(input())):
    s = input()
    a = []
    for i in s:
        a.append(int(i))
    re = 0
    n = len(a)
    for i in range(n-1,0,-1):
        a[i] += re
        re = a[i] // 10
        a[i] %= 10
        if a[i] >= 5:
            re = 1
        a[i] = 0

    a[0] += re
    for i in a:
        print(i, end = '')
    print()