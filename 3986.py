# 3986
# 좋은 단어
import sys
n = int(sys.stdin.readline())
count = 0

for _ in range(n):
    stack = []
    word = sys.stdin.readline().rstrip()
    for i in word:
        if len(stack)==0:
            stack.append(i)
        else:
            if stack[-1]==i:
                stack.pop()
            else:
                stack.append(i)
    
    if len(stack)==0:
        count += 1

print(count)