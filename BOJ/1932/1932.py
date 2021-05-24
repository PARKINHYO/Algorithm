import sys
import collections

triangle = []
N = int(sys.stdin.readline())
for i in range(N):
    triangle.append(list(map(int, sys.stdin.readline().split())))
dp = [[0]*500 for _ in range(500)]
for i in range(N):
    for j in range(i+1):
        if i == 0:
            dp[i][j] = triangle[0][0]
            continue
        if i == 1:
            dp[i][j] = dp[0][0] + triangle[i][j]
            continue
        dp[i][j] = max((triangle[i][j] + dp[i-1][j]),(triangle[i][j] + dp[i-1][j-1]))
print(max(dp[N-1]))
        
        
        