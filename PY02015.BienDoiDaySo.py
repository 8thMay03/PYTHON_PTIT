def count(a):
    if a[0] == a[1] == a[2] == a[3]:
        return 0
    x = []
    for i in range(4):
        x.append(abs(a[i] - a[(i + 1) % 4]))
    return count(x) + 1

while True:
    a = list(map(int, input().split()))
    if all(a[i] == 0 for i in range(4)):
        break
    print(count(a))