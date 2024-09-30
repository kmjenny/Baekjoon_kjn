# 10799
# 쇠막대기
import sys
razer = list(sys.stdin.readline().rstrip())
stack = []
count = 0

for i in range(len(razer)):
    if len(stack)==0:
        stack.append(razer[i])
    else:
        if stack[-1]!=razer[i]:
            stack.pop()
            if razer[i-1]!=razer[i]:
                count += len(stack)-1
            count += 1
        else:
            stack.append(razer[i])

print(count)