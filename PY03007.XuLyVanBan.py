from re import *

s = ""
while True:
    try:
        s += input()
    except:
        break

s = split(r'[\.\?\!]', s)

for i in s:
    x = i.lower().split()
    if len(x) > 0:
        x[0] = x[0].title()
    print(*x)
