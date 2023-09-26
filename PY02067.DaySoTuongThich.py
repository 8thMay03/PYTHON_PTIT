def check():  # Kiểm tra xem đúng yêu cầu đề bài chưa
    global a, b
    for i in range(n - 1):
        if (a[i] // b[i]) != (a[i + 1] // b[i + 1]):
            return False
    return True

def solve():
    global tmp
    for i in range(n):
        b[i] = a[i] // tmp
    while not check():
        tmp -= 1
        for i in range(n):
            b[i] = a[i] // tmp
    for i in range(n):
        while a[i] // b[i] == tmp:
            b[i] -= 1
        b[i] += 1

n = int(input())
a = list(map(int, input().split()))
tmp = min(a)
b = [0] * n
solve()
total_sum = sum(b)
print(total_sum)
