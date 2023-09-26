n = int(input())
a = []
s = 0
for _ in range(n):
    x = list(map(int, input().split()))
    a.append(x)
for i in range(0, n - 1):
    s += a[i][i + 1]
s += a[0][n-1]
s //= 2

ans = []

for i in range(n - 2):
    sum = 0
    for j in range(i + 1, n):
        sum += a[i][j]
    x = (sum - s) // (n - i - 2)
    ans.append(x)
    s -= x

ans.append(a[0][n-2]-ans[0])
ans.append(a[0][n-1]-ans[0])
print(*ans)
