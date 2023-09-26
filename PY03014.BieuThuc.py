for _ in range(int(input())):
    s = input()
    st = []
    ans = []
    tmp = 1
    for i in s:
        if i == '(':
            st.append(tmp)
            ans.append(tmp)
            tmp += 1
        elif i ==')':
            ans.append(st[-1])
            st.pop()
    print(*ans)