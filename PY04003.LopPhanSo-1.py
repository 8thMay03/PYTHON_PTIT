import math

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def Simplify(self):
        GCD = math.gcd(self.num, self.den)
        self.num //= GCD
        self.den //= GCD

n, d = map(int, input().split())
f = Fraction(n, d)
f.Simplify()
print(str(f.num) + '/' + str(f.den))