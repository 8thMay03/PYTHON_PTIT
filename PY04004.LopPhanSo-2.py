import math
from fractions import Fraction

class Fract:
    def __init__(self, n, d):
        self.n = n
        self.d = d
    def sum(self, b):
        x = Fraction(self.n, self.d)
        y = Fraction(b.n, b.d)
        x += y
        self.n = x.numerator
        self.d = x.denominator

a, b, c, d = list(map(int, input().split()))
x = Fract(a, b)
y = Fract(c, d)
x.sum(y)
print(str(x.n) + '/' + str(x.d))