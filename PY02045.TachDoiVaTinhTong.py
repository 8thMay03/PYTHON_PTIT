s = input()

while len(s) != 1:
    x = s[:len(s) // 2]
    y = s[len(x):]
    s = str(int(x) + int(y))
    print(s)
