def IsPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sol(s):
    n = ""
    n += s[-4:]
    n = int(n)
    if IsPrime(n):
        return "YES"
    return "NO"

for _ in range(int(input())):
    s = input()
    print(sol(s))