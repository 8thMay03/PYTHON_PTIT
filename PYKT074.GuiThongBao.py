for _ in range(int(input())):
    s = input().split()
    ans = s[0]
    for i in s[1:]:
        if len(ans) + len(i) >= 100:
            break
        ans += " " + i
    print(ans)