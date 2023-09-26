import math


def solve(n):
    sum = 0
    for i in n:
        sum += math.factorial(int(i))
    if sum == int(n):
        return "Yes"
    return "No"


t = int(input())

while t > 0:
    n = input()
    print(solve(n))
    t -= 1
