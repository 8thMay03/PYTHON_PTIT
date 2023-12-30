for _ in range(int(input())):
    n, m, u, v = map(int ,input().split())
    a = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int ,input().split())
        a[x].append(y)
    
    paths = []
    tmp = []
    vis = [False for _ in range(n + 1)]

    def Try(i):
        global v, vis, path, tmp
        vis[i] = True
        tmp.append(i)
        if i == v:
            paths.append(list(tmp))
            return
        for j in a[i]:
            if not vis[j]:
                Try(j)
                vis[j] = False
                tmp.pop()
    
    Try(u)

    ans = 0
    cnt = {}
    for path in paths:
        for i in path:
            cnt[i] = cnt.get(i, 0) + 1
    
    for i in range(n + 1):
        if i == u or i == v:
            continue
        if cnt.get(i, 0) == len(paths):
            ans += 1
    
    print(ans)