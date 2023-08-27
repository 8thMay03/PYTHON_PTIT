def sol(s):
    if len(s) < 3:
        return "no"
    s = s.lower()
    if s[len(s)-3:] != '.py':
        return "no"
    for i in s:
        if (ord(i) < ord('a') or ord(i) > ord('z')) and (i != '.' and i != '_'):
            return "no"
    return "yes"

s = input()
print(sol(s))