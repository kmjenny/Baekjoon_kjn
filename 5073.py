# 삼각형과 세 변
# 브론즈3
import sys
result = []

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    sum = a+b+c
    if a==b==c==0:
        break

    if a==b==c:
        result.append("Equilateral")
    elif max(a,b,c)>=sum-max(a,b,c):
        result.append("Invalid")
    elif a==b or a==c or b==c:
        result.append("Isosceles")
    else:
        result.append("Scalene")

for i in result:
    print(i)