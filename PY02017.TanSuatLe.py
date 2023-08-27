for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    for i in a:
        cnt[i] = cnt.get(i, 0) + 1
    for i in a:
        if cnt[i] % 2 == 1:
            print(i)
            break