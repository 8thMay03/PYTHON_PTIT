def IsPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def sol(s):
    a = s[:3]
    b = s[-3:]
    if IsPrime(int(a)) and IsPrime(int(b)):
        return "YES"
    return "NO"

for _ in range(int(input())):
    s = input()
    print(sol(s))