s = input()
ans = []
while len(s) >= 2:
    x = int(s[:2])
    ans.append(x)
    s = s[2:]
ans = sorted(set(ans))
print(*ans)

