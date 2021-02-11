"""
fixme. https://leetcode.com/problems/climbing-stairs/
fixme. 당신은 계단을 오르고 있다. 정상에 도달하기 위해 n 계단을 올라야 한다.
fixme. 매번 각각 1계단 또는 2계단씩 오를 수 있다면 정상에 도달하기 위한 방법은 몇가지 경로가 되는지 계산하라.
fixme. 입력 : 3
fixme. 출력 : 3
fixme. 설명
fixme. 정상에 오르기 위한 방법은 3가지 경로가 있다.
fixme. 1계단 + 1계단 + 1계단
fixme. 1계단 + 2계단
fixme. 2계단 + 1계단
"""

import collections

class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n<= 2:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]