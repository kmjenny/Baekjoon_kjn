# 5397
# 키로거
import sys

L = int(sys.stdin.readline())

for _ in range(L):
    st = list(sys.stdin.readline().rstrip())
    st1 = []
    st2 = []
    for i in st:
        if i=="<":
            if st1:
                st2.append(st1.pop())
        elif i==">":
            if st2:
                st1.append(st2.pop())
        elif i=="-":
            if st1:
                st1.pop()
        else:
            st1.append(i)
    
    st1.extend(reversed(st2))
    print(''.join(st1))
