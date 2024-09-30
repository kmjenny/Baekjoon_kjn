# 3273
# 두 수의 합
import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

minus = [x-i for i in num]

result = set(num).intersection(set(minus))

print(len(result)//2)