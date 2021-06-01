import sys
import bisect
input = sys.stdin.readline


N = int(input())
prog = list(map(int, input().split()))

# N이 1이면 답 1 출력
if N == 1:
    print(1)
    exit(0)

# answer 리스트에 수열 첫번째 값 넣고 두번째 부터 for문 돌림.
answer = [prog[0]]
for i in range(1, N):
    
    """
    answer배열에서  가장 오른쪽 값 즉, 
    가장 큰 값이 현재 수열 prog[i]보다 작으면
    prog[i]를 answer 가장 오른쪽으로 append.
    """
    if answer[-1] < prog[i]:
        answer.append(prog[i])
    
    # answer 가장 오른쪽 값이 더 크거나 같으면,
    # answer에서 prog[i]가 들어갈 인덱스를 찾은다음
    # 그 위치에 기존 값에서 prog[i]로 교체해줌.
    else:
        answer[bisect.bisect_left(answer, prog[i])] = prog[i]

# answer 배열 길이를 출력하면 답.
print(len(answer))
