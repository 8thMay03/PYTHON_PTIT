n, m = map(int, input().split())
a = list(map(int, input().split()))
cnt = {}

for i in a:
    cnt[i] = cnt.get(i, 0) + 1

b = list(cnt)
b.sort(key=lambda x: (cnt[x], x))

if cnt[b[0]] == cnt[b[-1]]:
    print("NONE")
else:
    idx = len(b) - 1
    while cnt[b[idx]] == cnt[b[-1]]:
        idx -= 1
    for i in b:
        if(cnt[i] == cnt[b[idx]]):
            print(i)
            break   