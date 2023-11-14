from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(A, B):
    return sqrt((A.x - B.x) ** 2 + (A.y - B.y) ** 2)

class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        
    def perimeter(self):
        a = distance(self.A, self.B)
        b = distance(self.A, self.C)
        c = distance(self.B, self.C)
        if a + b <= c or a + c <= b or b + c <= a or a * b * c == 0:
            return "INVALID"
        return '{:.3f}'.format(round(a + b + c, 3))

t = int(input())
a = []
for i in range(t):
    a += list(map(float, input().split()))

idx = 0
for i in range(t):
    A = Triangle(Point(a[idx], a[idx + 1]), Point(a[idx + 2], a[idx + 3]), Point(a[idx + 4], a[idx + 5]))
    print(A.perimeter())
    idx += 6