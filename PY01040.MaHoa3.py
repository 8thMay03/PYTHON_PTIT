def change(s):
    ans = ""
    val = 0
    for c in s:
        val += ord(c) - ord('A')
    for c in s:
        ans += chr((ord(c) - ord('A') + val) % 26 + ord('A'))
    return ans

for _ in range(int(input())):
    s = input()
    x = change(s[:len(s) // 2])
    y = change(s[len(s) // 2:])
    ans = ""
    for i in range(len(x)):
        ans += chr((ord(x[i]) + ord(y[i])- 2 * ord('A')) % 26 + ord('A'))
    print(ans)