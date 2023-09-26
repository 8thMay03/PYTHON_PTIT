for _ in range(int(input())):
    s = input()
    x = 0
    ans = []
    for i in s:
        if i.isdigit():
            x += int(i)
        if i.isalpha():
            ans.append(i)
    ans.sort()
    for i in ans:
        print(i, end = '')
    print(x)