s = input()
s = s[::-1]
ans = ""

for i in range(0,len(s)):
    if i != 0 and i % 3 == 0 :
        ans += ','
    ans += s[i]

ans = ans[::-1]
print(ans)