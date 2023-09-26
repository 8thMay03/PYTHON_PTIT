def check(n):
    s = str(n)
    return s == s[::-1] and len(s) > 1

a = []
n, m = map(int, input().split())
mx = 0

for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
    for j in x:
        if check(j):
            mx = max(mx, j)

if mx == 0:
    print("NOT FOUND")
else:
    print(mx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == mx:
                print("Vi tri [{}][{}]".format(i, j))