n = int(input())
sum1, sum2 = 0, 0

for i in range(n):
    x = list(map(int, input().split()))
    for j in range(n):
        if j < i:
            sum1 += x[j]
        elif j > i:
            sum2 += x[j]

k = int(input())
if abs(sum1 - sum2) <= k:
    print("YES")
    print(abs(sum1 - sum2))
else:
    print("NO")
    print(abs(sum1 - sum2))