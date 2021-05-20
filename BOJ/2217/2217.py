import sys

N = int(sys.stdin.readline())
weights = [int(sys.stdin.readline()) for x in range(N)]
weights.sort(reverse=True)

answer = 0
for i in range(N):
    answer = max(answer, weights[i]*(i+1))
print(answer) 