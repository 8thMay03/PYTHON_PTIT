dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0 ,1, -1, 1, -1, 0, 1]

n, m = map(int, input().split())
a = []
vis = [[0] * m for _ in range(n)] 
ans = 0     

for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            for k in range(8):
                ii = i + dx[k]
                jj = j + dy[k]
                if ii >= 0 and ii < n and jj >= 0 and jj < m and vis[ii][jj] == 0:
                    ans += a[ii][jj]
                    vis[ii][jj] = 1
            
print(ans)        