# 약수들의 합

n = int(input())
result = []

while n!=-1:
    test = []
    t = ""
    t = t+str(n)+" = 1"
    for i in range(2,n):
        if n%i==0:
            t = t + " + " + str(i)
            test.append(i)
    all_sum = 1
    for j in test:
        all_sum += int(j)
    if n==all_sum:
        result.append(t)
    else:
        k = ""
        k = k+str(n)+" is NOT perfect."
        result.append(k)

    n = int(input())

for i in result:
    print(i)