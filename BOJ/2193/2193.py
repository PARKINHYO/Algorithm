import sys, collections
input = sys.stdin.readline


class Solution:
    def pinary_number(self, N: int):
        if N == 1:
            return 1
        if N == 2:
            return 1
        dp = collections.defaultdict(int)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, N+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[N]


N = int(input())
print(Solution().pinary_number(N))