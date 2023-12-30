class Person:
    def __init__(self, name, number, date):
        self.name = name
        self.number = number
        self.date = date
        self.x = self.name.split()[-1]
    def __str__(self):
        return self.name + ": " + self.number + " " +  self.date

People = []
f = open('SOTAY.txt', 'r')
lines = f.read().split('\n')
f.close()

while len(lines) > 0:
    x = lines[0]
    lines = lines[1:]
    if x[:4] == 'Ngay':
        date = x[5:]
    else:
        name = x
        if len(lines) > 0:
            number = lines[0]
            lines = lines[1:]
            People.append(Person(name, number, date))

People.sort(key = lambda p : (p.x, p.name))

for person in People:
    print(person)