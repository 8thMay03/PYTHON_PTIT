def sol(n, p):
    cnt = 0
    i = p
    while i <= n:
        cnt += n//i
        i *= p
    return cnt

for _ in range(int(input())):
    n, p = map(int ,input().split())
    print(sol(n, p))