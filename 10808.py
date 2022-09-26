# 알파벳 개수
# a = 97
# z = 122
import sys
S = sys.stdin.readline()
all = [0 for i in range(26)]
for i in range(len(S)-1):
    all[ord(S[i])-97] += 1
for i in all:
    print(i, end=' ')