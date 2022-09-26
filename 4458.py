# 첫 글자를 대문자로
# a 097 A 065
# z 122 Z 090

import sys
N = int(sys.stdin.readline())
all = []
for i in range(N):
    word = sys.stdin.readline()
    if 97<=ord(word[0])<=122:
        x = ord(word[0])-32
        words=chr(x)+word[1:]
    else:
        words=word
    all.append(words)

for i in range(N):
    print(all[i],end='')