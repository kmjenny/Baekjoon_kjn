# 최소, 최대
import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(f'{min(nums)} {max(nums)}')