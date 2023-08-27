import math

t = int(input())
while t>0:
    n = int(input())
    list = []
    print("1 * ",end = "")
    for i in range(2,int(math.sqrt(n))):
        if n%i == 0:
            cnt = 0
            while n%i == 0:
                cnt += 1
                n //= i
            list.append(str(i)+'^'+str(cnt))
    if n!=1:
        list.append(str(n) + '^1')

    for i in range(0,len(list)-1):
        print(list[i] + ' * ',end = "")
    print(list[-1])
    t-= 1