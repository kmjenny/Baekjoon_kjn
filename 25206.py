# 너의 평점은
# 실버5

import sys
num = 0.0
all = 0.0
score = {'A+':4.5,
         'A0':4.0,
         'B+':3.5,
         'B0':3.0,
         'C+':2.5,
         'C0':2.0,
         'D+':1.5,
         'D0':1.0,
         'F':0.0}

for i in range(20):
    name, credit, grade = sys.stdin.readline().split()
    if grade == "P":
        continue
    else:
        credit = float(credit)
        all += credit
        num += score[grade] * credit

print("{:.6f}".format(num/all))
