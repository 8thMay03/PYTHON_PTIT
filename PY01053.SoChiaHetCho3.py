t = int(input())
while t>0:
    mod = 0
    s = input()
    for i in s:
        mod = (mod * 10 + int(i)) % 3
    if mod == 0:
        print("YES")
    else:
        print("NO")
    t -= 1 