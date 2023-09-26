while True:
    n = int(input())
    a = []
    if n == 0:
        break
    for _ in range(n):
        a.append(int(input()))
    a.sort()
    if a[n-1] == a[0]:
        print("BANG NHAU")
    else:
        print(a[0], a[n-1])