n, m = map(int, input().split())
mn, mx = 1000000, -1
a = []
ans = []

for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
    for j in x:
        mn = min(mn, j)
        mx = max(mx, j)

target = mx - mn
for i in range(n):
    for j in range(m):
        if a[i][j] == target:
            ans.append((i, j))

if len(ans) > 0:
    print(target)
    for i in ans:
        print("Vi tri [{}][{}]".format(i[0], i[1]))
else:
    print("NOT FOUND")