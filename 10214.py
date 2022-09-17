# Baseball

T = int(input())
result = []

for i in range(T):
    all_Y=0
    all_K=0
    for j in range(9):
        Y, K=map(int,input().split())
        all_Y += Y
        all_K += K
    if all_Y>all_K:
        result.append('Yonsei')
    elif all_Y<all_K:
        result.append('Korea')
    else:
        result.append('Draw')

for i in result:
    print(i)