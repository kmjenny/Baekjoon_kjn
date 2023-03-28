# 과제 안 내신 분..?
# 브론즈5

import sys
all = [i for i in range(1,31)]

for _ in range(28):
    num = int(sys.stdin.readline())
    all.remove(num)

print(min(all))
print(max(all))