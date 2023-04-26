# 숫자 카드
# 실버5
import sys
N = int(sys.stdin.readline())
card1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card2 = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in range(M):
    dic[card2[i]] = 0

for idx in range(N):
    if card1[idx] in dic.keys():
        dic[card1[idx]] += 1

print(*dic.values())