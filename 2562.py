# 최댓값
import sys
count=1
a = int(sys.stdin.readline())
for i in range(2,10):
    b = int(sys.stdin.readline())
    if a<b:
        a=b
        count=i
print(a)
print(count)