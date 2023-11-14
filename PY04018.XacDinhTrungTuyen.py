mp = {'1': 2.0, '2': 1.5, '3': 1.0, '4': 0}
mpp = {'A': 'TOAN', 'B': 'LY', 'C': 'HOA'}

class Teacher:
    def __init__(self, id, name, code, p1, p2):
        self.id = 'GV{:02d}'.format(id)
        self.name = name
        self.code = code
        self.p1 = p1
        self.p2 = p2
        self.total = p1 * 2 + p2 + mp[code[1]]
        if self.total >= 18:
            self.classify = 'TRUNG TUYEN'
        else:
            self.classify = 'LOAI'
    
    def __str__(self):
        return self.id + " " + self.name + " " + mpp[self.code[0]] + " " + str(self.total) + " " + self.classify

Teachers = []

for i in range(int(input())):
    name = input().strip()
    code = input()
    p1 = float(input())
    p2 = float(input())
    Teachers.append(Teacher(i + 1, name, code, p1, p2))

Teachers.sort(key=lambda t: -t.total)

for t in Teachers:
    print(t.__str__())