# 개표
# 입력 V(심사위원의 수) 각각 누구에게 투표(A,B는 참가자)
# 출력 A>B=>A, A<B=>B, A==B=>Tie

V = int(input())
result = list(input())

count = 0

for i in range(V):
    if result[i]=='A':
        count += 1

if V-count==count:
    print('Tie')
elif V-count>count:
    print('B')
else:
    print('A')