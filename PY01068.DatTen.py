n, k = map(int, input().split())
a = sorted(list(set(list(map(str, input().split())))))
x = []

def Try(i):
    for j in range(i, len(a)):
        x.append(a[j])
        if len(x) == k:
            print(*x)
        else:
            Try(j + 1)
        x.pop()
    
Try(0)