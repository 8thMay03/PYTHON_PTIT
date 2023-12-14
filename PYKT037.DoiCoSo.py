def sol(n, b):
    ans = ""
    while n > 0:
        remainder = n % b
        if remainder < 10:
            ans = str(remainder) + ans
        else:
            ans = chr(ord('A') + remainder - 10) + ans
        n //= b
    if ans == "":
        return "0"
    return ans

for _ in range(int(input())):
    n, b = map(int, input().split())
    ans = sol(n, b)
    print(ans)