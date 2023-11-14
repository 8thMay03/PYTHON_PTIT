n, m , x = map(int ,input().split())
adj = [[] for _ in range(n + 1)]
vis = [None for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int ,input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(u):
    global vis
    vis[u] = 1
    for v in adj[u]:
        if not vis[v]:
            dfs(v)

dfs(x)

for i in range(1, n + 1):
    if not vis[i]:
        print(i)