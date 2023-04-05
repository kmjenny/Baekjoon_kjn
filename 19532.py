# 수학은 비대면강의입니다
# 브론즈2
import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())

x = (c*e-f*b)//(a*e-d*b)
y = (c*d-f*a)//(b*d-e*a)
print(f"{x} {y}")