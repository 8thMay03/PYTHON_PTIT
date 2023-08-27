def check(s):
    if len(s)%2==1:
        return False
    for i in s:
        if int(i)&1:
            return False
    return s == s[::-1]

for _ in range(int(input())):
    n = int(input())
    for i in range(22,n,2):
        if check(str(i)) == True:
            print(i, end = " ")
    print()