# 화성수학
# 연산자 @(3을 곱하기), %(5를 더하기), #(7을 빼기)
# 입력 T(테스트의 개수)

T = int(input())
formula = list()
result = list()

for i in range(T):
    formula.append(input().split())
    number = float(formula[i][0])
    for j in range(1,len(formula[i])):
        if formula[i][j]=='@':
            number*=3
        elif formula[i][j]=='%':
            number+=5
        elif formula[i][j]=='#':
            number-=7
    result.append(number)

for i in result:
    print("{:.2f}".format(i))