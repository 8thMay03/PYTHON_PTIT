def sol(s):
    ss = s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(ss[i]) - ord(ss[i-1])):
            return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    print(sol(s))