def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def sol(n):
    s = 0
    for i in n:
        s += int(i)
    if IsPrime(s):
        return "YES"
    return "NO"

for _ in range(int(input())):
    n = input()
    print(sol(n))