t = int(input())

while t>0:
    s = input()
    x = "" + s[0] + s[1]
    y = "" + s[-2] + s[-1]
    if x==y:
        print("YES")
    else:
        print("NO")
    t -= 1
    
