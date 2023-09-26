s = input()
ans = []
while len(s) >= 2:
    x =s[:2]
    if x not in ans:
        ans.append(x)
    s = s[2:]
print(*ans)

