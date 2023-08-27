import math

def checkPrime(n):
    if n < 2:
        return "NO"
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return "NO"
    return "YES"

def sol(s):
    sum = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if int(s[i]) % 2 != 0 :
                return "NO"
        if i % 2 == 1:
            if int(s[i]) % 2 != 1 :
                return "NO"
        sum += int(s[i])
    return checkPrime(sum)

for _ in range(int(input())):
    s = input()
    print(sol(s))