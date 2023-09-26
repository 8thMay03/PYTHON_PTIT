class Participant:
    def __init__(self, name, date, grade):
        self.name = name
        self.date = date
        self.grade = grade

name = input()
date = input()
x = float(input())
y = float(input())
z = float(input())

A = Participant(name, date, x + y + z)
print("{} {} {:.1f}".format(A.name, A.date, A.grade))