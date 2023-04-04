# 알고리즘 수업 - 알고리즘의 수행 시간 6
# 브론즈2
import sys
n = int(sys.stdin.readline())
sum = 0
j = 1
for i in range(n-2,0,-1):
    sum += i*j
    j += 1
print(sum)
print("3")