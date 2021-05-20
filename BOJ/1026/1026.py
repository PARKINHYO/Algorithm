import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

tmp = B[:]

A.sort()
tmp.sort(reverse=True)

answer = 0
for i in range(N):
    answer += (A[i] * tmp[i])
print(answer)