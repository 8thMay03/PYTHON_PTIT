for _ in range(int(input())):
    print("Test " + str(_ + 1) + ": ", end="")
    s1 = input()
    s2 = input()
    c1 = [char for char in s1]
    c2 = [char for char in s2]
    c1.sort()
    c2.sort()
    if c1 == c2:
        print("YES")
    else:
        print("NO")