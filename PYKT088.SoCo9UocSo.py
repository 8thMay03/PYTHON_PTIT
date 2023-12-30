n, ans, i = int(input()), 0, 2
l = int(n ** (0.5))
a = [i for i in range(l + 1)]

# Xây dựng mảng a chứa các ước số nhỏ nhất của mỗi số từ 2 đến l
while i * i <= l:
    if a[i] == i:
        for j in range(i * i, l + 1, i):
            a[j] = i
    i += 1

# Đếm số lượng số có đúng 9 ước số
for i in range(2, l + 1):
    p = a[i]
    q = a[i // a[i]]
    if p * q == i and q != 1 and p != q:
        ans += 1
    if a[i] == i and i ** 8 <= n:
        ans += 1

print(ans)
