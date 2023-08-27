def sol(s):
    if len(s) < 3:
        return "NO"
    l = 0
    r = len(s) - 1
    while(int(s[l]) < int(s[l + 1])):
        l += 1
    while(int(s[r]) < int(s[r - 1])):
        r -= 1
    if l==r:
        return "YES"
    return "NO"

for _ in range(int(input())):
    s = input()
    print(sol(s))   