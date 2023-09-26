s = input()
k = int(input())
cnt = {}
while len(s) >= 2:
    x = s[:2]
    cnt[x] = cnt.get(x, 0) + 1
    s = s[2:]
ans = list(cnt)
ans.sort()
ok = 0
for i in ans:
    if cnt[i] >= k:
        print(i, cnt[i])
        ok = 1
if ok == 0:
    print("NOT FOUND")