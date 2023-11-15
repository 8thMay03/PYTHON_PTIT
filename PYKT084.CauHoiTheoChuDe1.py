cnt = 0
a = []

n = int(input())

for _ in range(n):
    s = input()
    a.append(s)

while '' in a:
    idx = a.index('')
    print(a[0] + ': ' + str(idx - 1))
    a = a[idx + 1:]

print(a[0] + ': ' + str(len(a) - 1))   