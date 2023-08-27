import math

def checkPrime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def SumDigit(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum

t = int(input())
while t>0:
    a,b = map(int,input().split())
    gcd = math.gcd(a,b)
    if checkPrime(SumDigit(gcd)) == True:
        print("YES")
    else:
        print("NO")
    t -= 1
