import sys, collections
input = sys.stdin.readline


class Solution:
    def fib(self, n: int):
        if n == 1:
            return 1
        if n == 2:
            return 1
        dp = collections.defaultdict(int)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


print(Solution().fib(int(input())))