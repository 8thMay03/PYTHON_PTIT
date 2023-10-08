class Complex:
    def __init__(self, realPart, virtualPart):
        self.realPart = realPart
        self.virtualPart = virtualPart

    def getStr(self):
        if self.virtualPart > 0:
            return str(round(self.realPart)) + " + " + str(round(self.virtualPart)) + "i"
        return str(round(self.realPart)) + " - " + str(round(-self.virtualPart)) + "i"

def sum_complex(a, b):
    realPart = a.realPart + b.realPart
    virtualPart = a.virtualPart + b.virtualPart
    return Complex(realPart, virtualPart)

def mul_complex(a1, a2):
    realPart = a1.realPart * a2.realPart - a1.virtualPart * a2.virtualPart
    virtualPart = a1.realPart * a2.virtualPart + a2.realPart * a1.virtualPart
    return Complex(realPart, virtualPart)

for _ in range(int(input())):
    a, b, c, d = map(float, input().split())
    A = Complex(a, b)
    B = Complex(c, d)
    result1 = mul_complex(sum_complex(A, B), A)
    result2 = mul_complex(sum_complex(A, B), sum_complex(A, B))
    print(result1.getStr() + ", " + result2.getStr())
