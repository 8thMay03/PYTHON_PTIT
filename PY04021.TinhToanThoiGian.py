class Gamer:
    def __init__(self, id, name, begin, end):
        self.id = id
        self.name = name
        self.begin = begin
        self.end = end
        self.totalTime = int(end[:2]) * 60 + int(end[3:]) - int(begin[:2]) * 60 - int(begin[3:])

    def output(self):
        print("{} {} {} gio {} phut".format(self.id, self.name, self.totalTime // 60, self.totalTime % 60 ))
    
Gamers = []
for _ in range(int(input())):
    id = input()
    name = input()
    begin = input()
    end = input()
    Gamers.append(Gamer(id, name, begin, end))

Gamers.sort(key=lambda x: -x.totalTime)

for i in Gamers:
    i.output()