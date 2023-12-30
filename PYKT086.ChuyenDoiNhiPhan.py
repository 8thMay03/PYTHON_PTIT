import math

f = open('DATA.in', 'r')

for _ in range(int(f.readline())):
    b = int(math.log2(int(f.readline())))
    s = f.readline().strip()
    while len(s) % b != 0:
        s = '0' + s
    ans = ''
    while len(s) > 0:
        x = s[len(s) - b:]
        x = x[::-1]
        s = s[:len(s) - b]
        tmp = 0
        for i in range(len(x)):
            tmp += (int(x[i]) * (2 ** i))
        if tmp >= 10:
            tmp = chr(ord('A') + (tmp % 10))
        ans = str(tmp) + ans
    print(ans)