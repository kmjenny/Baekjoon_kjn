# 네번째 점
# 입력 세 점의 좌표

A= list()
B= list()

for i in range(3):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

if A[0]==A[1]:
    result_a=A[2]
elif A[1]==A[2]:
    result_a=A[0]
else:
    result_a=A[1]

if B[0]==B[1]:
    result_b=B[2]
elif B[1]==B[2]:
    result_b=B[0]
else:
    result_b=B[1]

print(result_a,result_b)