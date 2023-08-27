a, k, n = map(int,input().split())

ok = 0
div = a % k

for i in range(k-div,n-a+1,k):
    ok = 1
    print(i, end = " ")
if ok == 0:
    print(-1)