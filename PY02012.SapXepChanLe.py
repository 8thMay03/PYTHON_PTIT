n = int(input())
a = list(map(int, input().split()))

while len(a) < n:
    b = list(map(int, input().split()))
    for i in b:
        a.append(i)

odd, even, ans = [], [], []

for i in range(n):
    if a[i]&1:
        odd.append(i)
    else:
        even.append(i)

odd.sort(key=lambda x: (a[x]), reverse=True)
even.sort(key=lambda x: (a[x]))
x, y = 0, 0
for i in range(n):
    if i in odd:
        ans.append(a[odd[x]])
        x += 1
    elif i in even:
        ans.append(a[even[y]])
        y += 1
print(*ans)
