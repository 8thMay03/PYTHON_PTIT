n = int(input())
a = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int ,input().split())
    a[x].append(y)
    a[y].append(x)

ans = "Yes"

for i in range(1, n + 1):
    if len(a[i]) != 1 and len(a[i]) != n - 1:
        ans = "No"
        break

print(ans)