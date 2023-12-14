for _ in range(int(input())):
    n, m, u, v = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    vis = [False for _ in range (n + 1)]
    tmp = []
    cnt = {}
    count = 0
    ans = 0

    for _ in range(m):
        x, y = map(int ,input().split())
        adj[x].append(y)
    
    def Try(i):
        global u, v, vis, adj, count
        vis[i] = True
        tmp.append(i)

        if i == v:
            count += 1
            for x in tmp:
                cnt[x] = cnt.get(x, 0) + 1

        for j in adj[i]:
            if not vis[j]:
                Try(j)
                vis[j] = False
                tmp.pop()
    
    Try(u)
    
    for i in range(1, n + 1):
        if i == u or i == v:
            continue
        if cnt.get(i, 0) == count:
            ans += 1
    
    print(ans)