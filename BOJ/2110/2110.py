import sys

# 문제 이해가 어렵군..

N, C = map(int, sys.stdin.readline().split())
loc = [int(sys.stdin.readline()) for _ in range(N)]
loc.sort()


if N == C:
    answer = sys.maxsize
    for i in range(1, N):
        answer = min(loc[i] - loc[i-1], answer)
    print(answer)
else:
    jump = N // C+1
    answer = sys.maxsize
    for i in range(jump, N,jump):
        answer = min(loc[i] - loc[i-jump], answer)
    print(answer)