from sys import stdin
from collections import defaultdict


class Solution:
    def fib(self, N: int):
        if N == 0:
            print(1, 0)
            return
        if N == 1: 
            print(0, 1)
            return
        dp = [[0, 0] for x in range(N+1)]
        dp[0][0], dp[0][1] = 1, 0
        dp[1][0], dp[1][1] = 0, 1
        for i in range(2, N+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0]
            dp[i][1] = dp[i-1][1] + dp[i-2][1]

        print(dp[N][0], dp[N][1])
        return


for _ in range(int(stdin.readline())):
    Solution().fib(int(stdin.readline()))
