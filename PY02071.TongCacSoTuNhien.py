for _ in range(int(input())):
    n = int(input())
    ans, v = [], []

    def Try(i, s):
        global ans, v, n
        for j in range(i, 0, -1):
            v.append(j)
            if s + j == n:
                ans.append(list(v))
            elif s + j < n:
                Try(j, s + j)
            v.pop()

    Try(n, 0)
    print(len(ans))
    for lst in ans:
        print("(", end='')
        print(*lst, end='')
        print(')', end=' ')
    print()