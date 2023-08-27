n = int(input())
a = (list(map(int,input().split())))

ans = []
for i in a:
    if len(ans) == 0:
        ans.append(i)
    else:
        if (ans[-1] + i) % 2 == 0:
            ans.pop()
        else:
            ans.append(i)

print(len(ans))