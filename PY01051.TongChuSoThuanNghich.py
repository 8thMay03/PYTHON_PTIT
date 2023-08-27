def sol(s):
    sum = 0
    for i in s:
        sum += int(i)
    sum = str(sum)
    if(sum == sum[::-1] and len(sum) > 1):
        return "YES"
    return "NO"

for _ in range(int(input())):
    s = input()
    print(sol(s))