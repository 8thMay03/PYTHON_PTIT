def sol(s):
    a = [str for str in s.split(".")]
    if len(a) != 4:
        return "NO"
    for i in a:
        try:
            num = int(i)
            if num < 0 or num > 255:
                return "NO"
        except ValueError:
            return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    print(sol(s))
