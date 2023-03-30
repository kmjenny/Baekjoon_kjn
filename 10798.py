# 세로읽기
# 브론즈1

import sys
words = []
for i in range(5):
    word = sys.stdin.readline().rstrip()
    word = word.ljust(15,'#')
    words.append(word)

for i in range(15):
    for j in range(5):
        if words[j][i]=="#":
            continue
        else:
            print(words[j][i], end="")