# 문자열
import sys
T = int(sys.stdin.readline())
all = []
for i in range(T):
    word = input()
    word = word[0]+word[-1]
    all.append(word)
for i in all:
    print(i)