# 회사에 있는 사람
# 실버5
import sys
n = int(sys.stdin.readline())
log = set()

for i in range(n):
    name, state = sys.stdin.readline().split()
    if name not in log and state=="enter":
        log.add(name)
    elif name in log and state=="leave":
        log.remove(name)

log_list = sorted(log, reverse=True)
for i in log_list:
    print(i)
