import sys


N = int(sys.stdin.readline())
RGBs = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N)]



for i in range(N):
    if i == 0:
        dp[i][0] = RGBs[i][0]
        dp[i][1] = RGBs[i][1]
        dp[i][2] = RGBs[i][2]
        continue
    dp[i][0] = RGBs[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = RGBs[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = RGBs[i][2] + min(dp[i-1][0], dp[i-1][1])

tmp = min(dp[-1][0], dp[-1][1])
print(min(tmp, dp[-1][2]))


    
    