# TGN
# 입력 N:테스트 케이스의 개수
# N개의 줄 -> r(광고X 수익), e(광고O 수익), c(광고 비용)
# 출력 광고O(advertise), 광고X(do not advertise), 차이X(does not matter)

N = int(input())
result = []

for i in range(N):
    r, e, c = map(int, input().split())
    if e-c>r:
        result.append('advertise')
    elif e-c==r:
        result.append('does not matter')
    else:
        result.append('do not advertise')

for i in range(N):
    print(result[i])