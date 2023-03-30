# 최댓값
# 브론즈3

import sys
nums = []
for i in range(9):
    num = list(map(int, sys.stdin.readline().split()))
    nums.append(num)

max_num = max(map(max, nums))

for i in range(9):
    for j in range(9):
        if max_num == nums[i][j]:
            max_i = i
            max_j = j
            break

print(max_num)
print(f"{max_i+1} {max_j+1}")