from datetime import datetime

class Racer:
    def __init__(self, name, address, endTime):
        self.name = name
        self.address = address
        self.endTime = endTime
        self.time = (datetime.strptime(endTime, '%H:%M') - datetime.strptime('06:00', '%H:%M')).seconds / 3600
        self.speed = 120 / self.time
        self.id = ''
        for i in self.address.split():
            self.id += i[0]
        for i in self.name.split():
            self.id += i[0]

    def __str__(self):
        return self.id + " " + self.name + " " + self.address + " " + str(round(self.speed)) + " Km/h"

Racers = []

for _ in range(int(input())):
    name = input().strip()
    address = input().strip()
    endTime = input().strip()
    Racers.append(Racer(name, address, endTime))

Racers.sort(key=lambda r: -r.speed)

for r in Racers:
    print(r.__str__())