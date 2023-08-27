t = int(input())

while t>0:
    s = input()
    ans = 0
    s += '#'
    x = 0
    for i in s:
        if i.isdigit():
            x = x*10 + int(i)
        else:
            ans = max(ans,x)
            x = 0
    print(ans)
    t-=1