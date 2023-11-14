words1 = open('DATA1.in', 'r').read().lower().split()
words2 = open('DATA2.in', 'r').read().lower().split()

ans1, ans2 = set(), set()

for char in words1:
    if char not in words2:
        ans1.add(char)

for char in words2:
    if char not in words1:
        ans2.add(char)

print(*sorted(ans1))
print(*sorted(ans2))