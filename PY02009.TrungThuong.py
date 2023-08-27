for _ in range(int(input())):
    cnt = {}
    a = []
    for __ in range(int(input())):
        n = int(input())
        cnt[n] = cnt.get(n, 0) + 1
    
    ans = 1001
    app = 0
    for i in cnt:
        if app == cnt[i]:
            if ans > i:
                ans = i
        elif app < cnt[i]:
            app = cnt[i]
            ans = i
        
    print(ans)