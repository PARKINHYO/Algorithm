import heapq
import sys
input = sys.stdin.readline


Q = []
N = int(input())
for _ in range(N):
    heapq.heappush(Q, int(input()))

if N == 1:
    print(heapq.heappop(Q))
    exit(0)
    print(heapq.heappop(Q) + heapq.heappop(Q))
    exit(0)
else:
    answers = []
    while Q and len(Q) != 1:
        print(answers)
        answers.append(heapq.heappop(Q) + heapq.heappop(Q))
        heapq.heappush(Q, answers[-1])
print(sum(answers))