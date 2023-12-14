def SumDigit(n):
    sum = 0
    for c in n:
        sum += int(c)
    return str(sum)

n = input()
ans = 0

while len(n) != 1:
    n = SumDigit(n)
    ans += 1
print(ans)