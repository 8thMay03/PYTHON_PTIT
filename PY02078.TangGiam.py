for _ in range(int(input())):
    n = int(input())
    a, b = [], []
    dp = [1] * n

    for __ in range(n):
        x, y = map(float, input().split())
        a.append(x)
        b.append(y)
    
    for i in range(n):
        for j in range(i):
            if(a[i] > a[j] and b[i] < b[j]):
                dp[i] = max(dp[j] + 1, dp[i])
    
    dp.sort()
    print(dp[-1])
