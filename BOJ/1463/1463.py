from sys import stdin
from collections import defaultdict


class Solution:
    dp = defaultdict(int)

    def makeOne(self, N: int):

        self.dp[1] = 0

        for i in range(2, N+1):
            candidates = []
            if i % 3 == 0:
                candidates.append(self.dp[i//3] + 1)
            if i % 2 == 0:
                candidates.append(self.dp[i//2] + 1)
            candidates.append(self.dp[i-1] + 1)
            self.dp[i] = min(candidates)
        return self.dp[N]


print(Solution().makeOne(int(stdin.readline())))
