# 분해합
# 브론즈2
import sys
N = int(sys.stdin.readline())
all = []
for i in range(1,N):
    num = i
    first = i

    while True:
        next_num = i%10
        i = i//10
        num += next_num
        if i==0:
            break

    if num == N:
        all.append(first)
        break

if len(all)==0:
    print("0")
else:
    print(all[0])