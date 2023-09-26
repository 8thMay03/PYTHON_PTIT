for _ in range(int(input())):
    n, m, l = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    i = j = k = ok = 0
    while i < n and j < m and k < l:
        if a[i] == b[j] and b[j] == c[k]:
            print(a[i], end=' ')
            i += 1
            j += 1
            k += 1
            ok = 1
        elif a[i] > b[j]:
            j += 1
        elif b[j] > c[k]:
            k += 1
        else:
            i += 1
    if ok == 0:
        print("NO", end='')
    print()