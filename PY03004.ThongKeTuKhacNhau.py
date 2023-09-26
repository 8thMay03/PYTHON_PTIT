import re

cnt = {}
a = set()

for _ in range(int(input())):
    line = input().strip().lower()
    words = re.findall(r'\b\w+\b', line)
    for word in words:
        word = word.strip()  
        if word:
            cnt[word] = cnt.get(word, 0) + 1
            a.add(word)

a = sorted(a, key=lambda word: (-cnt[word], word))
for word in a:
    print(word, cnt[word])