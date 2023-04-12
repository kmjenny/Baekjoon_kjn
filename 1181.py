# 단어 정렬
# 실버5
import sys
N = int(sys.stdin.readline())
word = set()
for _ in range(N):
    word.add(sys.stdin.readline().rstrip())
word = list(word)
word.sort()
result = sorted(word, key=lambda x : len(x))

for i in result:
    print(i)