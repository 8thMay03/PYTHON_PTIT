n = int(input())
a = ['2', '3', '5', '7']

def check(s):
    cnt2, cnt3, cnt5, cnt7 = 0, 0, 0, 0
    for c in s:
        if c != '2' and c != '3' and c != '5' and c != '7':
            return False
        if c == '2':
            cnt2 += 1
        if c == '3':
            cnt3 += 1
        if c == '5':
            cnt5 += 1
        if c == '7':
            cnt7 += 1
    if cnt2 * cnt3 * cnt5 * cnt7 == 0:
        return False

    if int(s[-1]) % 2 == 0:
        return False
    return True

def Try(s):
    global m
    for c in a:
        if len(s) == m - 1:
            if check(s + c):
                print(s + c)
        else:
            Try(s + c)

for m in range(4, n + 1):
    Try("")