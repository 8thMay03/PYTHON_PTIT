for _ in range(int(input())):
    n, m = map(int, input().split())
    a, b, ans = [], [], 0

    for __ in range(n):
        a.append(list(map(int, input().split())))
    for __ in range(3):
        b.append(list(map(int, input().split())))

    for i in range(n - 2):
        for j in range(m - 2):
            for ii in range(3):
                for jj in range(3):
                    ans += a[i + ii][j + jj] * b[ii][jj]
    
    print(ans)