import math

def checkPrime(n):
    if n < 2:
        return "NO"
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return "NO"
    return "YES"

t = int(input())

while t>0:
    n = int(input())
    k = 0
    for i in range(1,n):
        if(math.gcd(i, n) == 1):
            k += 1
    print(checkPrime(k))
    t -= 1