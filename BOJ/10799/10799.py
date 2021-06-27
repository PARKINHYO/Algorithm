import sys
input = sys.stdin.readline

bar_razor = list(input().rstrip())
answer = 0
stack = []

for i in range(len(bar_razor)):
    if bar_razor[i] == '(': #스택 쌓기
        stack.append('(')
    else:
        if bar_razor[i-1] == '(': #()라면 (를 pop하고 현재 스택에 들어있는 ( 수만큼 값을 더해준다.
            stack.pop()
            answer += len(stack)
        else:
            stack.pop() 
            answer += 1 #끄트머리 막대기 부분을 더해준다
print(answer)

