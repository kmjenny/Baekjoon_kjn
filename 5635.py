# 생일
n=int(input())
all_people = []

for i in range(n):
    names, b_day, b_mon, b_year = input().split()
    each_peo = []
    each_peo.append(names)
    each_peo.append(int(b_day))
    each_peo.append(int(b_mon))
    each_peo.append(int(b_year))
    all_people.append(each_peo)

all_people.sort(key=lambda x:(x[3],x[2],x[1]))

print(all_people[n-1][0])
print(all_people[0][0])