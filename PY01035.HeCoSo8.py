s = input()
ans = ""
while len(s)%3 != 0:
    s = '0' + s
while len(s) > 0:
    tmp = 0
    tmp += int(s[-1]) + int(s[-2])*2 + int(s[-3])*4
    ans = str(tmp) + ans
    s = s[:-3]    
print(ans)