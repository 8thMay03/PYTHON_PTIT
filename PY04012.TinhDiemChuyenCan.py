class Student:
    def __init__(self, id, name, cla):
        self.id = id
        self.name = name
        self.cla = cla
    def cal(self, s):
        m = s.count('m')
        v = s.count('v')
        self.p = max(0, 10 - m - v * 2)
    def output(self):
        print(self.id + " " + self.name + " " + self.cla + " " + str(self.p), end='')
        if self.p == 0:
            print(" KDDK", end='')
        print()

a = {}
n = int(input())

for _ in range(n):
    x = Student(input(), input(), input())
    a[x.id] = x

for _ in range(n):
    id, status = input().split()
    a[id].cal(status)

for i in a:
    a[i].output()