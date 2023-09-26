lst = []
a = [1] * 10001
a[0] = a[1] = 0

for i in range(2, 10001):
    if a[i] == 1:
        lst.append(i)
        for j in range(i*i, 10001, i):
            a[j] = 0

ans = 0
n = int(input())
x = list(map(int, input().split()))
for i in x:
    if a[i] != 1:
        id = 0
        while lst[id] < i:
            id += 1
        cnt1 = lst[id] - i
        cnt2 = i - lst[id-1]
        ans = max(min(cnt1, cnt2), ans)

print(ans)