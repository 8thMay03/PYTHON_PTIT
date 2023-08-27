def solve(s):
    if(len(s)==1):
        print("NO")
    elif s[-2] == '8' and s[-1] == '6':
        print ("YES")
    else: 
        print("NO")

t = int(input())
while t > 0:
    s = input()
    solve(s)
    t -= 1
