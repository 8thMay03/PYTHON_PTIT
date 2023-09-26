a = [str for str in input().lower().split()]
b = [str for str in input().lower().split()]
ans1, ans2 = [], []

for i in a:
    if i not in ans1:
        ans1.append(i)
    if i in a and i in b:
        ans2.append(i)

for i in b:
    if i not in ans1:
        ans1.append(i)

print(*sorted(ans1))
print(*sorted(set(ans2)))