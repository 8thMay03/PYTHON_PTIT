import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        diff = max(a[i], a[i + 1]) / min(a[i], a[i + 1])
        if math.ceil(math.log2(diff)) >= 1:
            ans += math.ceil(math.log2(diff)) - 1
    print(ans)