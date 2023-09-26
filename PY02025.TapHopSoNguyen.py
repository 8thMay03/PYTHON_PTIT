n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt1 = [0] * 1001
cnt2 = [0] * 1001

for i in a:
    cnt1[i] += 1
for i in b:
    cnt2[i] += 1

for i in range(1, 1001):
    if cnt1[i] > 0 and cnt2[i] > 0:
        print(i, end = ' ')
print()

for i in range(1,1001):
    if cnt1[i] > 0 and cnt2[i] == 0:
        print(i, end = ' ')
print()

for i in range(1,1001):
    if cnt1[i] == 0 and cnt2[i] > 0:
        print(i, end = ' ')
