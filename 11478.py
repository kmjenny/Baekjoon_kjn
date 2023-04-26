# 서로 다른 부분 문자열의 개수
# 실버3
import sys
S = sys.stdin.readline().rstrip()
all = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        all.add(S[i:j+1])

print(len(all))