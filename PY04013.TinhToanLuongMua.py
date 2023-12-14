from datetime import datetime
import math

cntTime = {}
cntWater = {}
station_list = []
name_list = []
cnt = 1

class Station:
    def __init__(self, name):
        self.name = name
        self.id = "T{:02d}".format(cnt)
    
    def __str__(self):
        return self.id + " " + self.name + " " + "{:.2f}".format(round(cntWater[self.name] / cntTime[self.name], 2))
        
for _ in range(int(input())):
    name = input()
    t1 = input()
    t2 = input()
    water = int(input())
    if name not in name_list:
        station_list.append(Station(name))
        name_list.append(name)
        cnt += 1
    cntTime[name] = cntTime.get(name, 0) + (datetime.strptime(t2, '%H:%M') - datetime.strptime(t1, '%H:%M')).seconds / 3600
    cntWater[name] = cntWater.get(name, 0) + water

for station in station_list:
    print(station.__str__())