for _ in range(int(input())):
    n = int(input())
    a = list(map(int ,input().split()))
    R, L = [0] * n, [0] * n
    ans = 0

    L[0] = a[0]
    for i in range(1, n):
        L[i] = max(a[i], L[i - 1])

    R[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        R[i] = min(a[i], R[i + 1])
    
    for i in range(0, n):
        if i == 0:
            if a[i] < R[i + 1]:
                ans += 1
        elif i == n - 1:
            if a[i] == L[i]:
                ans += 1
        else:
            if a[i] == L[i] and a[i] < R[i + 1]:
                ans += 1
    
    print(ans)
