for _ in range(int(input())):
    a = []
    for __ in range(int(input())):
        x, y = map(int, input().split())
        a.append((x, y))

    a.sort(key=lambda x:x[1])
    last = a[0][1]
    ans = 1

    for i in range(1, len(a)):
        if a[i][0] >= last:
            ans += 1
            last = a[i][1]
    
    print(ans)