# 열 개씩 끊어 출력하기
import sys
N = sys.stdin.readline()
for i in range(len(N)-1):
    if i%10==0 and i!=0:
        print()
        print(N[i],end='')
    else:
        print(N[i],end='')