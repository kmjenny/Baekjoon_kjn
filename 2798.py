# 블랙잭
# 브론즈2
import sys
N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

card = 0
card_sum = 0

for i in range(N):
    for j in range(i+1,N):
        for z in range(j+1,N):
            num_sum = num[i]+num[j]+num[z]
            if card_sum<num_sum<=M:
                card_sum = num_sum

print(card_sum)