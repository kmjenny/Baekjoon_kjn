# 진법 변환
# 브론즈2

import sys
N, B = sys.stdin.readline().split()
B = int(B)

length = len(N)
num = 0

if B==10:
    print(N)
elif B<10:
    N_list = list(N)
    N_list.reverse()
    N = ''.join(N_list)
    for i in range(length):
        n = int(N[i])
        num += n*(B**i)
    print(num)
elif B>10:
    N_list = list(N)
    N_list.reverse()
    N = ''.join(N_list)
    for i in range(length):
        if 65<=ord(N[i])<=90: # 문자인 경우
            n = ord(N[i])-55
            num += n*(B**i)
        else:
            n = int(N[i])
            num += n*(B**i)
    print(num)
