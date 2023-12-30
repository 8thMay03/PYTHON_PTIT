from datetime import datetime

class Cathi:
    def __init__(self, id, date ,room):
        self.id = "C{:03d}".format(id)
        self.date = date
        self.room = room
    
    def __str__(self):
        return self.id + " " + self.date + " " + self.room

f = open('CATHI.in', 'r')        

lst = []

for id in range(int(f.readline())):
    date = f.readline().strip() + ' ' + f.readline().strip()
    room = f.readline().strip()
    lst.append(Cathi(id + 1, date, room))

lst.sort(key = lambda x : (datetime.strptime(x.date, '%d/%m/%Y %H:%M'), x.id))
for i in lst:
    print(i)