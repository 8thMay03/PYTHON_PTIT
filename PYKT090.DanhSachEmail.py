line = open('CONTACT.in', 'r')
a = {i.strip().lower() for i in line}
a = list(sorted(a))
for i in a:
    print(i)