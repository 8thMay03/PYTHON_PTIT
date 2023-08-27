fb = []
fb.append(0)
fb.append(1)
for i in range(2,94):
    fb.append(fb[i-1] + fb[i-2])

for _ in range(int(input())):
    a, b = map(int,input().split())
    for i in range(a,b+1):
        print(fb[i], end = " ")
    print()