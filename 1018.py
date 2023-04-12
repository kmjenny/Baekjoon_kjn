# 체스판 다시 칠하기
# 실버4
import sys
N, M = map(int, sys.stdin.readline().split())
chess = []
for i in range(N):
    word = sys.stdin.readline().rstrip()
    chess.append(word)

num = []

for i in range(N-7):
    for j in range(M-7):
        d1 = 0
        d2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2==0:
                    if chess[a][b]!='B':
                        d1 += 1
                    if chess[a][b]!='W':
                        d2 += 1
                else:
                    if chess[a][b]!='W':
                        d1 += 1
                    if chess[a][b]!='B':
                        d2 += 1
        num.append(d1)
        num.append(d2)

print(min(num))