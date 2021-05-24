import sys
import collections


N = int(sys.stdin.readline())
scores = [int(sys.stdin.readline()) for _ in range(N)]
dp = collections.defaultdict(int)

# 문제를 제대로 읽자..

for i in range(N):
    if i == 0:
        dp[0] = scores[0]
        continue
    if i == 1:
        dp[1] = scores[0] + scores[1]
        continue
    if i == 2:
        dp[2] = max((scores[0] + scores[2]), (scores[1] + scores[2]))
        continue
    # 바로 전 칸에서 올라오는경우 현재 점수, 전 점수, 전전 dp값 더하기
    # 두칸 전에서 올라오는 경우는 현재 점수에 두칸전 dp 더하기
    # 위에 두개 중 최대 값 
    dp[i] = max((scores[i] + scores[i-1] + dp[i-3]), (scores[i] + dp[i-2]))
print(dp[N-1])