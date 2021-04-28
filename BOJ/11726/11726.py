from sys import stdin
from collections import defaultdict


class Solution:
    def tiling(self, n: int):
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = defaultdict(int)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] % 10007


print(Solution().tiling(int(stdin.readline())))
