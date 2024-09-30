# 1919
# 애너그램 만들기
import sys
a = list(sys.stdin.readline().strip())
b = list(sys.stdin.readline().strip())
a1, b1 = a[:], b[:]
a2 = a
print(a1)
print(a2)
x = [i for i in a if not i in b1 or b1.remove(i)]
y = [i for i in b if not i in a1 or a1.remove(i)]
print(len(x)+len(y))