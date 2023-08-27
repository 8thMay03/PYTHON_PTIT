t = int(input())
while t>0:
    s = input()
    for i in range(1,len(s),2):
            print(s[i-1]*int(s[i]),end = '')
    print()
    t -= 1  