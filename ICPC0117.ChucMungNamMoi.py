import math

t = int(input())
a = []

while t>0:
    n = input()
    if n not in a:
        a.append(n)
    t -= 1

print(len(a))