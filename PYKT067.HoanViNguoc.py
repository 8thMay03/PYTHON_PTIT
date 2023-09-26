from itertools import permutations

for _ in range(int(input())):
    n = int(input())
    s = ""
    for i in range(1, n + 1):
        s += str(i)
    ans = list(permutations(s))
    ans = ans[::-1]
    print(len(ans))
    for i in ans:
        print(''.join(i), end=' ')
    print()