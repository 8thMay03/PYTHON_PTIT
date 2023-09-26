n, m = map(int, input().split())
a = []
for _ in range(n):
    x = list(map(int, input().split()))
    a.append(x)
if n > m:
    for i in range(n - m):
        a.pop(i)
else:
    for lst in a:
        for i in range(m - n):
            lst.pop(i + 1)
for lst in a:
    print(*lst)