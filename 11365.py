# !밀비 급일
import sys
word = sys.stdin.readline().rstrip()
all = []
while word!='END':
    words = word[::-1]
    all.append(words)
    word = sys.stdin.readline().rstrip()
for i in all:
    print(i)