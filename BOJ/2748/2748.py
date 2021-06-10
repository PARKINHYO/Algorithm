import sys
input = sys.stdin.readline
import collections


n = int(input())
if n == 1:
    print(1)
    exit(0)

dp = collections.defaultdict(int)
dp[0], dp[1] = 0, 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])