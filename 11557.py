# Yangjojang of The Year

T = int(input())
result = []

for i in range(T):
    beers = 0
    schools = ""
    N = int(input())
    for j in range(N):
        school, beer = input().split()
        if beers<int(beer):
            beers=int(beer)
            schools = school
    result.append(schools)

for i in result:
    print(i)