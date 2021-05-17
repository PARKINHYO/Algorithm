import sys

M, N = map(int, sys.stdin.readline().split())
S = []
for _ in range(M):
    S.append(input())

count = 0
for _ in range(N):
    if input() in S:
        count +=1
print(count)