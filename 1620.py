# 나는야 포켓몬 마스터 이다솜
# 실버4
import sys
N, M = map(int, sys.stdin.readline().split())
monster = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    monster[i+1] = name
    monster[name] = i+1

for i in range(M):
    question = sys.stdin.readline().rstrip()
    if question.isdigit():
        print(monster[int(question)])
    else:
        print(monster[question])
