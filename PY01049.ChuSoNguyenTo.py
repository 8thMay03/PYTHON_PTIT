def IsPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sol(s):
    if IsPrime(len(s)) == False:
        return "NO"
    prime = 0
    for i in s:
        if i == '2' or i == '3' or i=='5' or i=='7':
            prime += 1
        else:
            prime -= 1
    if prime > 0:
        return "YES"
    return "NO"

for _ in range(int(input())):
    s = input()
    print(sol(s))