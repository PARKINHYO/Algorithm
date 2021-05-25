import sys
N, K = map(int, sys.stdin.readline().split())
students = [0]*N
dp = [0]*21
cnt = 0
for rank in range(N):
    l = len(sys.stdin.readline().rstrip())
    students[rank] = l
    if rank > K:
        dp[students[rank-K-1]] -= 1
    cnt += dp[l]
    dp[l] += 1
print(cnt)