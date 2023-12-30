mp = {6 : 1, 8 : 1, 7 : 2}
pre = 0
ans = []
sentences = []

for _ in range(int(input())):
    sentences.append(input())

while len(sentences) > 0:
    length = len(sentences[0].split())
    if mp[length] != pre:
        pre = mp[length]
        ans.append(pre)
        if pre == 2:
            sentences = sentences[3:]
            pre = 0
    sentences = sentences[1:]

print(len(ans))
for i in ans:
    print(i)