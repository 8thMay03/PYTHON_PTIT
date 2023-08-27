def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n%i == 0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    ans = []

    def check(s):
        ss = s[::-1]
        if int(ss) > n or ss == s:
            return False
        if IsPrime(int(ss)) and IsPrime(int(s)):
            return True
        return False

    for i in range(n):
        if check(str(i)):
            if str(i) not in ans:
                ans.append(str(i))
                ans.append(str(i)[::-1])
    for i in ans:
        print(i, end = ' ')
    print()