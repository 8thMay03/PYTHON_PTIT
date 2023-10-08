file = open('DATA.in', 'r')

lst = []

for line in file:
    datas = line.strip().split()
    for data in datas:
        try:
            x = int(data)
            if x > 10 ** 9:
                lst.append(data)
        except:
            lst.append(data)

print(*sorted(lst))