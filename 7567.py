# 그릇
# 그릇 높이 : 10cm
# 같은 방향의 그릇 : +5cm
# 다른 방향의 그릇 : +10cm

plates = list(input())
height = 10

for i in range(len(plates)-1):
    if plates[i]==plates[i+1]:
        height += 5
    else:
        height += 10

print(height)