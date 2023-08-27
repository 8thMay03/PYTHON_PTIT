for _ in range(int(input())):
    n = int(input())
    ans = -1
    tmp = 0
    cnt = {}
    a = list(map(int, input().split()))
    
    for i in range(n):
        cnt[a[i]] = cnt.get(a[i], 0) + 1
    st = set(a)
    for i in st:
        if cnt[i] > n // 2:
            if tmp < cnt[i]:
                tmp = cnt[i]
                ans = i
    
    if ans > 0:
        print(ans)
    else:
        print("NO")