a, ans, v = [], [], []

def Try(i):
    for j in range(i, len(a)):
        v.append(a[j])
        if len(v) == k:
            ans.append(list(v))
        else:
            Try(j + 1)
        v.pop()

n, k = map(int, input().split())
x = list(map(int, input().split()))
a = list(set(x))
a.sort()
Try(0)

for lis in ans:
    print(*lis)
