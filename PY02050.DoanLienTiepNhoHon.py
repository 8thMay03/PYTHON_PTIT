for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans, st = [], []
    
    for i in range(n):
        while len(st) > 0 and a[st[-1]] <= a[i]:
            st.pop()
        if len(st) == 0:
            ans.append(i + 1)
        else:
            ans.append(i - st[-1])
        st.append(i)
    print(*ans)