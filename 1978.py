# 소수 찾기
import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
count=0
for i in range(N):
    if nums[i]!=1:
        for j in range(2,nums[i]):
            if nums[i]%j==0:
                count-=1
                break
        count+=1
print(count)