def IsPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sol(s):
    for i in range(len(s)):
        if IsPrime(i) == True:
            if IsPrime(int(s[i])) == False:
                return "NO"
        else:
            if IsPrime(int(s[i])) == True:
                return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    print(sol(s))