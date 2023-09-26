class person:
    def __init__(self, id, name, grade):
        self.id = "TS0" + str(id)
        self.name = name
        self.grade = grade
        if self.grade >= 9.5:
            self.typ = "XUAT SAC"
        elif self.grade >= 8.0:
            self.typ = "DAT"
        elif self.grade >= 5.0:
            self.typ = "CAN NHAC"
        else:
            self.typ = "TRUOT"

lst = []

for i in range(int(input())):
    name = input()
    a = float(input())
    b = float(input())
    if a > 10:
        a /= 10
    if b > 10:
        b /= 10
    lst.append(person(i + 1, name, (a + b) / 2))

lst.sort(key=lambda x : (-x.grade))
for i in lst:
    print(i.id + " " + i.name + " " + "{:.2f}".format(i.grade) + " " + i.typ)