n, x = map(int, input().split())
a = [1] * 200005
a[0] = a[1] = 0
prime = []

i = 2
while len(prime) < n + 1:
    if a[i] == 1:
        prime.append(i)
        for j in range(i * i, 200005, i):
            a[j] = 0
    i += 1

for i in range(n + 1):
    print(x, end=' ')
    x += prime[i]