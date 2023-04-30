# 균형 잡힌 세상
# 실버4
import sys
def check(c):
    a=[]
    for i in range(len(c)):
        if c[i]=="(" or c[i]=="[":
            a.append(c[i])
        elif c[i]==")":
            if len(a)==0:
                return "no"
            elif a[len(a)-1]=="(":
                del a[len(a)-1]
            else:
                return "no"
        elif c[i]=="]":
            if len(a)==0:
                return "no"
            elif a[len(a)-1]=="[":
                del a[len(a)-1]
            else:
                return "no"

    if len(a)==0:
        return "yes"
    else:
        return "no"


while True:
    word = sys.stdin.readline().rstrip()
    if word == ".":
        break
    else:
       result = check(word)
       print(result)