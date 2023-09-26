def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
b = {}
for i in a:
    b[i] = 1

a = list(b)
n = len(a)
ans = "NOT FOUND"

for i in range(1, n):
    a[i] += a[i - 1] 

for i in range(n - 1):
    if IsPrime(a[i]) and IsPrime(a[n - 1] - a[i]):
        ans = i
        break
print(ans)