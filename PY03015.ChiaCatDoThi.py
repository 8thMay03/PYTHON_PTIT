from queue import Queue

for _ in range(int(input())):
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    vis = [False for _ in range (n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
    
    def dfs(u):
        global vis, adj
        vis[u] = True
        for v in adj[u]:
            if not vis[v]:
                dfs(v)
    
    def count():
        global vis, adj
        cnt = 0
        for i in range(1, n + 1):
            if not vis[i]:
                cnt += 1
                dfs(i)
        return cnt

    mx = 1
    ans = 0
    for i in range(1, n + 1):
        vis = [False for _ in range (n + 1)]
        vis[i] = True
        tmp = count()
        if ans < i and mx < tmp:
            ans = i
            mx = tmp

    print(ans)