def sol(s):
    a = []
    for i in s:
        if i not in a:
            a.append(i)
    if len(a) != 2:
        return "NO"
    for i in range(0,len(s)-2):
        if s[i] != s[i+2]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    print(sol(s))