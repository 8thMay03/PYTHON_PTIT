def sol(s):
    for i in s:
        if i != '1' and i != '2' and i != '0':
            return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    print(sol(s))
