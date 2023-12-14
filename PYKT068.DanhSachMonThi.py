class Subject:
    def __init__(self, id, name, form):
        self.id = id
        self.name = name
        self.form = form
    
    def __str__(self):
        return ("{} {} {}").format(self.id, self.name, self.form)
    
Subjects = []

for _ in range(int(input())):
    Subjects.append(Subject(input(), input(), input()))

Subjects.sort(key=lambda x: x.id)

for Subject in Subjects:
    print(Subject.__str__())