def solve(s):
    sum = 0
    for i in range(0,len(s)):
        sum += int(s[i])
        if i < len(s)-1:
            if abs(int(s[i]) - int(s[i+1])) != 2:
                return "NO"
    if sum%10 != 0:
        return "NO"
    return "YES"

t = int(input())
while t > 0:
    s = input()
    print(solve(s))
    t -= 1