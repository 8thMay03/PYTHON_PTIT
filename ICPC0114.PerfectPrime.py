import math

def IsPrime(n):
    if n<2:
        return -1
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            return -1
    return 1

def solve(n):
    if IsPrime(n)!=1:
        return "No"
    m = str(n)
    reversed(m)
    x = int(m)
    if IsPrime(x)!=1:
        return "No"
    s = 0
    for i in m:
        if i!='2' and i!='3' and i!='5' and i!='7':
            return "No"
        else:
            s += int(i)
    if IsPrime(s) != 1:
        return "No"
    return "Yes"

t = int(input())

while t>0:
    n = int(input())
    print(solve(n))
    t -= 1