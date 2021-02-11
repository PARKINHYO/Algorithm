"""
fixme. https://leetcode.com/problems/fibonacci-number/
fixme. Q85. 피보나치 수
fixme. 피보나치 수를 구하라.
fixme. 입력 : n = 2
fixme. 출력 : 1
"""
import collections
import numpy as np


class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

    dp = collections.defaultdict(int)

    def fibMemorization(self, N: int) -> int:
        if N <= 1:
            return N

        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]

    def fibTabulation(self, N: int) -> int:
        self.dp[1] = 1

        for i in range(2, N + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[N]

    def fibTwoVariable(self, N: int) -> int:
        x, y = 0, 1
        for i in range(0, N):
            x, y = y, x + y
        return x

    def fibNumpy(self, n):
        M = np.matrix([0, 1], [1, 1])
        vec = np.array([0], [1])

        return np.matmul(M ** n, vec)[0]
