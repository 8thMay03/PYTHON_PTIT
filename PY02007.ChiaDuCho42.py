a = []
ans = []

while len(a) < 10:
    a += (list(map(int, input().split())))

for i in a:
    x = i % 42
    if x not in ans:
        ans.append(x)

print(len(ans))