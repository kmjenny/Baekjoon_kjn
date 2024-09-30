# 1406
# 에디터
import sys

# 배열, 링크드리스트 시간 초과
# 커서를 기준으로 왼쪽, 오른쪽 스택을 생성해서 넣기

st1 = list(sys.stdin.readline().rstrip()) # 왼쪽 스택
st2 = [] # 오른쪽 스택

num = int(sys.stdin.readline())

for i in range(num):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'L':
        if st1: # 문자열은 내용이 있을 때 참, 없을 때 거짓
            st2.append(st1.pop()) # 마지막꺼 꺼내서 오른쪽에 넣기 -> 커서 왼쪽 이동
    elif cmd[0] == 'D':
        if st2:
            st1.append(st2.pop())
            # pop이 가능한 이유 -> st2는 뒤에부터 들어가 있으니까 pop하면 제일 앞에 문자가 나옴
    elif cmd[0] == 'B':
        if st1:
            st1.pop()
    elif cmd[0] == 'P':
        st1.append(cmd[1])

st1.extend(reversed(st2)) # st2는 거꾸로 있는 상태니까 돌려서 더하기
print(''.join(st1))
    
