for _ in range(int(input())):
    s = input() + '!'
    ans = ""
    cnt = 0
    x = s[0]
    for i in range(len(s)):
        if s[i] == x:
            cnt += 1
        else:
            ans += (str(cnt) + x)
            x = s[i]
            cnt = 1
    print(ans)