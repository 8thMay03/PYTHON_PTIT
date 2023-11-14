from datetime import datetime

class Customer:
    def __init__(self, id, name, room, firstDay, lastDay, service):
        self.id = 'KH{:02d}'.format(id)
        self.name = name
        self.room = room
        self.firstDay = firstDay
        self.lastDay = lastDay
        self.service = service
        date1 = datetime.strptime(firstDay, '%d/%m/%Y')
        date2 = datetime.strptime(lastDay, '%d/%m/%Y')
        self.days = (date2 - date1).days + 1

    def total(self):
        if self.room[0] == '1':
            return self.days * 25 + self.service
        if self.room[0] == '2':
            return self.days * 34 + self.service
        if self.room[0] == '3':
            return self.days * 50 + self.service
        if self.room[0] == '4':
            return self.days * 80 + self.service

    def Str(self):
        return self.id + " " + self.name + " " + self.room + " " + str(self.days) + " " + str(self.total())

Customers = []

for i in range(int(input())):
    name = input().strip()
    room = input().strip()
    firstDay = input().strip()
    lastDay = input().strip()
    service = int(input())
    Customers.append(Customer(i + 1, name, room, firstDay, lastDay, service))

Customers.sort(key=lambda c: -c.total())

for c in Customers:
    print(c.Str())
