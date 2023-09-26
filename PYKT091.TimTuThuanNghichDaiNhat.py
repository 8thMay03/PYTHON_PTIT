import re

cnt = {}
mx = 0

file = open('VANBAN.in', 'r')

for line in file:
    words = line.split()
    for word in words:
        if word == word[::-1]:
            mx = max(mx, len(word))
            cnt[word] = cnt.get(word, 0) + 1

for i in cnt:
    if len(i) == mx:
        print(i, cnt[i])