# 대소문자 바꾸기
# a 097 A 065
# z 122 Z 090

import sys
word = sys.stdin.readline()
all = []
for i in range(len(word)-1):
    if 97<=ord(word[i])<=122:
        x = ord(word[i])-32
        all.append(chr(x))
    else:
        x = ord(word[i])+32
        all.append(chr(x))
for i in all:
    print(i, end='')
