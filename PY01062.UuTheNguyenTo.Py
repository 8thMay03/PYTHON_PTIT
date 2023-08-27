def IsPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def sol(s):
    if not IsPrime(len(s)):
        return "NO"
    cnt = 0
    for i in s:
        if IsPrime(int(i)):
            cnt += 1
        else:
            cnt -= 1
    if cnt > 0:
        return "YES"
    return "NO"

for _ in range(int(input())):
    s = input()
    print(sol(s))