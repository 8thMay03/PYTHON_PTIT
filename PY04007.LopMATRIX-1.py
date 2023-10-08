class Matrix:
    def __init__(self, row, column, a):
        self.row = row
        self.column = column
        self.a = a

    def transposeMatrix(self):
        row = self.column
        column = self.row
        b = [[0 for _ in range(column)] for _ in range(row)]

        for i in range(row):
            for j in range(column):
                b[i][j] = self.a[j][i]

        return Matrix(row, column, b)

    def output(self):
        for i in range(self.row):
            print(*self.a[i])

def mul(A, B):
    result = [[0 for _ in range(B.column)] for _ in range(A.row)]

    for i in range(A.row):
        for j in range(A.row):
            result[i][j] = sum(A.a[i][k] * B.a[k][j] for k in range(A.column))

    return Matrix(A.row, B.column, result)

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        x = list(map(int, input().split()))
        a.append(x)
    A = Matrix(n, m, a)
    B = A.transposeMatrix()
    C = mul(A, B)
    C.output()
