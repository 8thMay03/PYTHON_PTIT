n = int(input())
a = list(map(int, input().split()))
ans = 10000000000
x = -1
for i in a:
    target = i
    cnt = 0
    for j in a:
        cnt += abs(j - target)
    if(ans > cnt):
        ans = cnt
        x = target
print(ans, x)
