t = int(input())

while t>0:
    s = input()
    ans = 10**18
    s += '#'
    x = 0
    for i in s:
        if i.isdigit():
            x = x*10 +int(i)
        elif i.isalpha() and x>0:
            ans = min(ans,x)
            x = 0
    print(ans)
    t-=1