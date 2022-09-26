# 알파벳 찾기
import sys
S = sys.stdin.readline()
all = [-1 for i in range(26)]
for i in range(len(S)-1):
    x = ord(S[i])
    if all[x-97]==-1:
        all[x-97]=i
for i in all:
    print(i, end=' ')

# a = 97
# z = 122