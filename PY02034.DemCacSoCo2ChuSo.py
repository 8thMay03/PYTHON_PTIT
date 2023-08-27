n = input()
if len(n)%2 == 1:
    n = n[:-1]
a = []
cnt = {}

for i in range(0,len(n)-1,2):
    s = ""
    s += n[i] + n[i + 1]
    cnt[s] = cnt.get(s, 0) + 1

for i in cnt:
    print(i, cnt[i])    