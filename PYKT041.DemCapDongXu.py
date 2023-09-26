n = int(input())
a = []
ans = 0

for _ in range(n):
    a.append(input())

for i in range(n):
    for j in range(n - 1):
        if a[i][j] != 'C':
            continue
        for k in range(j + 1, n):
            if a[i][k] == 'C':
                ans += 1
for i in range(n - 1):
    for j in range(i + 1, n):
        for k in range(n):
            if a[i][k] != 'C':
                continue
            if a[j][k] == 'C':
                ans += 1
print(ans)
