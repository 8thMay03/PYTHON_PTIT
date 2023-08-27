class Student:
    def __init__(self, name, num1, num2):
        self.name = name
        self.num1 = num1
        self.num2 = num2
    def output(self):
        print(self.name, self.num1, self.num2)

lst = []

for _ in range(int(input())):
    x = input()
    y, z = map(int, input().split())
    A = Student(x, y, z)
    lst.append(A)

lst.sort(key = lambda x: ((-1)*x.num1, x.num2, x.name))

for i in lst:
    i.output()