# 팰린드롬인지 확인하기
# 앞으로 읽을 때와 거꾸로 읽을때 똑같은 단어
# 팰린드롬이면 1 아니면 0

word = list(input())
length = len(word)
count = 0

for i in range(int(length/2)):
    if word[i]==word[length-i-1]:
        count+=1
if count==int(length/2):
    print('1')
else:
    print('0')

