def sol(s):
    sum, mul, cnt0, cnt = 0, 1, 0, 0
    for i in range(len(s)):
        if i%2 == 0:
            sum += int(s[i])
        else:
            cnt += 1
            if s[i] == '0':
                cnt0 += 1
            if s[i] != '0':
                mul *= int(s[i])
    if cnt0 == cnt:
        mul = 0
    return sum, mul

for _ in range(int(input())):
    s = input()
    print(sol(s)[0], sol(s)[1])

    