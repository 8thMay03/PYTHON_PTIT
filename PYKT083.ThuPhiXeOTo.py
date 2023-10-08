cnt = {}

for _ in range(int(input())):
    s = input().split()
    if s[3] == 'IN':
        if s[1] == 'Xe_con':
            if s[2] == '5':
                cnt[s[-1]] = cnt.get(s[-1], 0) + 10000
            elif s[2] == '7':
                cnt[s[-1]] = cnt.get(s[-1], 0) + 15000
        elif s[1] == 'Xe_tai':
            cnt[s[-1]] = cnt.get(s[-1], 0) + 20000
        elif s[1] == 'Xe_khach':
            if s[2] == '29':
                cnt[s[-1]] = cnt.get(s[-1], 0) + 50000
            else:
                cnt[s[-1]] = cnt.get(s[-1], 0) + 70000

for x in cnt:
    print(x + ': ' + str(cnt[x]))