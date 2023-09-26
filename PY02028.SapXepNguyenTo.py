def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
prime, idx = [], []

for i in range(n):
    if IsPrime(a[i]):
        prime.append(a[i])
        idx.append(i)

prime.sort()
for i in range(n):
    if i not in idx:
        print(a[i], end=' ')
    else:
        print(prime[0], end=' ')
        prime.pop(0)
        idx.remove(i)