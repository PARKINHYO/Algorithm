import sys, collections
input = sys.stdin.readline


class Solution:
    def tiling(self, n: int):
        dp = collections.defaultdict(int)
        dp[1], dp[2] = 1, 3
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]*2
        return dp[n]%10007

print(Solution().tiling(int(input())))