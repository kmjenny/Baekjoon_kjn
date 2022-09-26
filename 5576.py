# 콘테스트
import sys
w = []
k = []
for i in range(20):
    x = int(sys.stdin.readline())
    if 0<=i<=9:
        w.append(x)
    elif 10<=i<=19:
        k.append(x)
w.sort(reverse=True)
k.sort(reverse=True)
print(w[0]+w[1]+w[2], k[0]+k[1]+k[2])