# 모음의 개수
import sys
word = sys.stdin.readline()
count=0
for i in range(len(word)-1):
    if word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u':
        count += 1
print(count)