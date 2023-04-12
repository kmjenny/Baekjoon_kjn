# 영화감독 숌
# 실버5
import sys
N = int(sys.stdin.readline())

first = 666

while N != 0:
    if '666' in str(first):
        N = N-1
        if N==0:
            break
    first = first + 1

print(first)