# 통계학
# 실버3
import sys
from collections import Counter
N = int(sys.stdin.readline())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()
check = Counter(num)
mode = check.most_common()
maximum = mode[0][1]

modes = []
for x in mode:
    if x[1] == maximum:
        modes.append(x[0])

print(round(sum(num)/len(num)))
print(num[N//2])
if len(modes)>1:
    print(modes[1])
else:
    print(modes[0])
print(max(num)-min(num))