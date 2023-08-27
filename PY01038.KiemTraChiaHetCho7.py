def sol(s):
    if s%7 == 0:
        return s
    cnt = 0
    while cnt <= 1000:
        ss = int(str(s)[::-1])
        s += ss
        if s%7 == 0:
            return s
        cnt += 1
    return -1

for _ in range(int(input())):
    s = int(input())
    print(sol(s))

        