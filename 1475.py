# 1475
# 배열
import sys
N = list(map(int,str(sys.stdin.readline().rstrip())))
num = [0]*10

for i in N:
    if i == 6 or i == 9:
        if num[6] <= num[9]:
            num[6] += 1
        else:
            num[9] += 1
    else:
        num[i] += 1

print(max(num))