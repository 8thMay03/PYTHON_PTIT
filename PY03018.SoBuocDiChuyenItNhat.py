from collections import deque

directions = [(0, 1), (1, 0), (1, 1)]

def sol(n, m, a):
    vis = [[0] * m for _ in range(n)]
    q = deque([((0, 0), 0)])
    vis[0][0] = 1

    while q:
        (x, y), step = q.popleft()

        if y + 1 < m:
            diff = abs(a[x][y] - a[x][y + 1])
            if y + diff < m and not vis[x][y + diff]:
                if x == n - 1 and y + diff == m - 1:
                    return step + 1
                q.append(((x, y + diff), step + 1))
                vis[x][y + diff] = 1

        if x + 1 < n:
            diff = abs(a[x][y] - a[x + 1][y])
            if x + diff < n and not vis[x + diff][y]:
                if x + diff == n - 1 and y == m - 1:
                    return step + 1
                q.append(((x + diff, y), step + 1))
                vis[x + diff][y] = 1

        if x + 1 < n and y + 1 < m:
            diff = abs(a[x + 1][y + 1] - a[x][y])
            if x + diff < n and y + diff < m and not vis[x + diff][y + diff]:
                if x + diff == n - 1 and y + diff == m - 1:
                    return step + 1
                q.append(((x + diff, y + diff), step + 1))
                vis[x + diff][y + diff] = 1

    return -1

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        x = list(map(int, input().split()))
        a.append(x)
    print(sol(n, m, a))