n = int(input())
a = list(map(int, input().split()))

while len(a) < n:
    b = list(map(int, input().split()))
    for i in b:
        a.append(i)

if a[n - 1] == n:
    print("Excellent!")
else:
    f = [int for int in range(1, a[n - 1] + 1)]
    for i in a:
        if i in f:
            f.remove(i)
    for i in f:
        print(i)