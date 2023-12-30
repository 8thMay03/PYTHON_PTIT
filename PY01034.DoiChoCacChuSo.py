def sol(s):
    a = [int(i) for i in s]
    i = len(a) - 1
    while i > 0 and a[i] >= a[i - 1]:
        i -= 1
    if i == 0:
        return -1

    i -= 1
    mx = -1
    idx = None

    for j in range(len(a) - 1, i, - 1):
        if a[j] >= mx and a[i] > a[j]:
            mx = a[j]
            idx = j
    
    if idx == None:
        return -1

    tmp = a[i]
    a[i] = a[idx]
    a[idx] = tmp

    if a[0] == 0:
        return -1
    a = [str(i) for i in a]
    return ''.join(a)

for _ in range(int(input())):
    print(sol(input()))
