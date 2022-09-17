# 소음
# 입력 A(양의 정수), 연산자, B(양의 정수) => 10의 제곱 형태, 최대 100자리

def calculate_quiz(A, B, C):
    if C == '+':
        A = A+B
    elif C == '*':
        A = A*B
    print(A)

A = int(input())
C = input()
B = int(input())

calculate_quiz(A, B, C)

