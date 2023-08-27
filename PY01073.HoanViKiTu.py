from itertools import permutations

s = input()
ans = list(permutations(s))

for i in ans:
    print(''.join(i))
