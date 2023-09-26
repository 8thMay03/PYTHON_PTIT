a = [0]*26
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(26):
    a[i] = 2**i - 1
for _ in range(int(input())):
    n, k = map(int, input().split())
    while n > 0:
        if k == 2 ** (n - 1):
            print(s[n - 1])
            break
        if k > a[n - 1]:
            k -= 2 ** (n - 1)
        n -= 1