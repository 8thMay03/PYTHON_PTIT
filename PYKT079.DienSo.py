for _ in range(int(input())):
    n = int(input())
    a = list(set(list(map(int, input().split()))))
    a.sort()
    l, r = a[0], a[-1]
    lst = [int for int in range(l, r+1)]
    for i in a:
        if i in lst:
            lst.remove(i)
    print(len(lst))