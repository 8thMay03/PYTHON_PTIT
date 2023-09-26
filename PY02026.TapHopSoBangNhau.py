n, m = map(int, input().split())
a = sorted(set(list(map(int ,input().split()))))
b = sorted(set(list(map(int ,input().split()))))
if a == b:
    print("YES")
else:
    print("NO")