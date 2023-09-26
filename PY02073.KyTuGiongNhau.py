for _ in range(int(input())):
    n = int(input())
    x, y, z = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[1] = x
    for i in range(2, n + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i // 2] + z, dp[i - 1] + x)
        else:
            dp[i] = min(dp[(i + 1) // 2] + y + z, dp[i - 1] + x)
    print(dp[n])