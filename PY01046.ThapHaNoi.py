import math

def Try(n, x, y, z):
    if n==1:
        print(x + ' -> ' + z)
        return
    Try(n-1, x, z, y)
    Try(1, x, y, z)
    Try(n-1, y, x, z)

n = int(input())
Try(n, 'A', 'B', 'C')