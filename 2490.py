# 윷놀이
import sys
result = []
for i in range(3):
    a = list(sys.stdin.readline())
    zero = a.count('0')
    one = a.count('1')
    if zero==0:
        result.append('E')
    elif zero==1:
        result.append('A')
    elif zero==2:
        result.append('B')
    elif zero==3:
        result.append('C')
    else:
        result.append('D')
for i in result:
    print(i)
