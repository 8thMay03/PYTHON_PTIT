def check(s):
    for i in range(0,len(s)-1):
        if s[i] > s[i+1]:
            return "NO"
    return "YES"

t = int(input())
while t>0:
    s = input()
    print(check(s))
    t -= 1