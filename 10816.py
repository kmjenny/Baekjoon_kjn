# 숫자 카드 2
# 실버4
import sys
N = int(sys.stdin.readline())
card1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card2 = list(map(int, sys.stdin.readline().split()))

hashmap = {}

for x in card1:
    if x in hashmap:
        hashmap[x] += 1
    else:
        hashmap[x] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in card2))