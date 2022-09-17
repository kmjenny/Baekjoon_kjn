# 0=not cute/ 1=cute
# 입력 N:설문조사를 한 사람 수
# 0 귀엽지 않음 1 귀여움
# 출력 0이 많으면 Junhee is not cute! 1이 많으면 Junhee is cute!

N = int(input())
count = 0
for i in range(N):
    result = int(input())
    if result == 0:
        count += 1

if count>N-count:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')