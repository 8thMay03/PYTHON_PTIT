n = int(input())
a = list(map(float, input().split()))
ans = 0
cnt = 0
a.sort()

for i in a:
    if i != a[0] and i != a[-1]:
        ans += i
        cnt += 1

print('{:.2f}'.format(ans/cnt))