# 창문 닫기
# 실버5
import sys
N = int(sys.stdin.readline())
window = 0
i = 1
while True:
    if i*i > N:
        break
    else:
        window+=1
        i+=1

print(window)