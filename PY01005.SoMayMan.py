def solve(n):
    cnt4 = 0
    cnt7 = 0
    for i in n:
        if i == '4':
            cnt4 += 1
        if i == '7':
            cnt7 += 1
    if cnt4 + cnt7 == 4 or cnt4 + cnt7 == 7:
        return "YES"
    return "NO"

n = input()
print(solve(n))

    