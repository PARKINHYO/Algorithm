from sys import stdin
from collections import defaultdict

class Solution:
    def sumOneTwoThree(self, N: int):
        dp = defaultdict(int)
        
        dp[1], dp[2], dp[3] = 1, 2, 4
        
        for i in range(4, N+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[N]


for _ in range(int(stdin.readline())):
    print(Solution().sumOneTwoThree(int(stdin.readline())))     