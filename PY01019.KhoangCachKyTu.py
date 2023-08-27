import math

def ans(s1,s2):
    for i in range(0,len(s1)-1):
        if abs(ord(s1[i]) - ord(s1[i+1])) != abs(ord(s2[i]) - ord(s2[i+1])):
            return "NO"
    return "YES"

t = int(input())
while t > 0:
    s1 = input()
    s2 = s1[::-1]
    print(ans(s1,s2))
    t -= 1