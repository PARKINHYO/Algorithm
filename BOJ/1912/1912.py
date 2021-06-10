import sys
input = sys.stdin.readline


n = int(input())
prog = list(map(int, input().split()))
dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = max(dp[i-1] + prog[i], prog[i])
print(max(dp))
# 너무 꼬아서 생각하지 말자..