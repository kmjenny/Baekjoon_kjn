# 인사성 밝은 곰곰이
# 실버4
import sys
N = int(sys.stdin.readline())
chat = set()
all = 0

for i in range(N):
    word = sys.stdin.readline().rstrip()
    if word == "ENTER":
        all += len(chat)
        chat = set()
    else:
        chat.add(word)

all += len(chat)
print(all)


