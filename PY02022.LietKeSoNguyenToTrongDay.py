def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
cnt = [0 for _ in range(max(a) + 1)]

for i in a:
    cnt[i] += 1
    
for i in a:
    if IsPrime(i):
        if cnt[i] > 0:
            print(i, cnt[i])
        cnt[i] = 0
