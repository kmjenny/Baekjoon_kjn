# 삼각형 외우기
# 브론즈4
import sys
all = []
for i in range(3):
    num = int(sys.stdin.readline())
    all.append(num)

if all[0]==all[1]==all[2]==60:
    print("Equilateral")
elif sum(all)==180:
    if all[0]==all[1] or all[0]==all[2] or all[1]==all[2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")