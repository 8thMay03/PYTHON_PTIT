def IsPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(2, n + 1):
        if IsPrime(i) and i < n - 6:
            if IsPrime(i + 6):
                if IsPrime(i + 2) or IsPrime(i + 4):
                    ans += 1
    print(ans)