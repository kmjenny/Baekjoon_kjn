# 나머지
import sys
remain = []
for i in range(10):
    x = int(sys.stdin.readline())
    remain.append(x%42)

s = set(remain) # set : 자료형의 중복을 제거하기 위한 필터 역할
print(len(s))
