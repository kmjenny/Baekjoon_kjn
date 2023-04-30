# 스택
# 실버4
import sys
N = int(sys.stdin.readline())
stack = []

def push(x):
    stack.append(x)
def pop():
    if len(stack)==0:
        print("-1")
    else:
        x = stack[len(stack)-1]
        del stack[len(stack)-1]
        print(x)
def size():
    print(len(stack))
def empty():
    if len(stack)==0:
        print("1")
    else:
        print("0")
def top():
    if len(stack)==0:
        print("-1")
    else:
        print(stack[len(stack)-1])

for i in range(N):
    a = sys.stdin.readline().rstrip()

    if 'push' in a:
        y = a[5:]
        push(y)
    else:
        if 'pop' == a:
            pop()
        elif 'size' == a:
            size()
        elif 'empty' == a:
            empty()
        elif 'top' == a:
            top()