# 괄호
# 실버4
import sys
T = int(sys.stdin.readline())
def check(x, y):
    for i in range(len(y)):
        if y[i] == "(":
            x.append(y[i])
        elif len(x)==0:
            return "NO"
        else:
            del x[len(x)-1]

    if len(x)==0:
        return "YES"
    else:
        return "NO"


for i in range(T):
    stack = []
    word = sys.stdin.readline().rstrip()

    a = check(stack, word)
    print(a)
