def sol(s):
    while len(s) > 0:
        if s.find('688') == 0:
            s = s[3:]
        elif s.find('68') == 0:
            s = s[2:]
        elif s.find('6') == 0:
            s = s[1:]
        else:
            return "NO"
    return "YES"

s = input()
print(sol(s))