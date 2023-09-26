import math

def grade(a):
    if 39 <= a <= 40:
        return 9.0
    elif a >= 37:
        return 8.5
    elif a >= 35:
        return 8.0
    elif a >= 33:
        return 7.5
    elif a >= 30:
        return 7.0
    elif a >= 27:
        return 6.5
    elif a >= 23:
        return 6.0
    elif a >= 20:
        return 5.5
    elif a >= 16:
        return 5.0
    elif a >= 13:
        return 4.5
    elif a >= 10:
        return 4.0
    elif a >= 7:
        return 3.5
    elif a >= 5:
        return 3.0
    elif a >= 3:
        return 2.5
    return 1.0 

for _ in range(int(input())):
    a, b, c, d = map(float, input().split())
    a = grade(a)
    b = grade(b)
    x = (a + b + c + d) / 4
    if x - int(x) >= 0.75:
        x = int(x) + 1
    elif x - int(x) >= 0.25:
        x = int(x) + 0.5
    else:
        x = int(x)
    print("{:.1f}".format(x))