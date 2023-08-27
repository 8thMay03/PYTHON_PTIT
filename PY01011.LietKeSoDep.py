def check(s):
    if len(s) % 2 == 1:
        return False
    ss = s[::-1]
    if ss!=s:
        return False
    for i in s:
        if int(i)%2==1:
            return False
    return True

t = int(input())
while t>0:
    n = int(input())
    for i in range(22,n):
        if check(str(i)) == True:
            print(i, end = " ")
    print()
    t -= 1