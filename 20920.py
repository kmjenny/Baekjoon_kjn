# 영단어 암기는 괴로워
# 실버3
import sys
from collections import Counter
N, M = map(int, sys.stdin.readline().split())
word = []
for i in range(N):
    a = sys.stdin.readline().rstrip()
    if len(a)>=M:
        word.append(a)

check = Counter(word)
check = sorted(check.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))

list_word = []
for i in range(len(check)):
    list_word.append(check[i][0])

for i in list_word:
    print(i)

