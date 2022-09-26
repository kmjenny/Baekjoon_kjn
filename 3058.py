# 짝수를 찾아라
import sys
T = int(sys.stdin.readline())
all = []
small = []
for i in range(T):
    even_nums = []
    nums = list(map(int,sys.stdin.readline().split()))
    for j in nums:
        if j%2==0:
            even_nums.append(j)
    all.append(sum(even_nums))
    small.append(min(even_nums))

for i in range(T):
    print(f"{all[i]} {small[i]}")
