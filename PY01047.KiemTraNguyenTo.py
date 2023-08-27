import math

def checkPrime(n):
    if n < 2:
        return "NO"
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return "NO"
    return "YES"

t = int(input())
while t > 0:
    s = input()
    n = s[-4:]
    n = int(n)
    print(checkPrime(n))
    t -= 1