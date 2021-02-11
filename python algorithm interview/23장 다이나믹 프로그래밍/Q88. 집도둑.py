"""
fixme. https://leetcode.com/problems/house-robber/
fixme. Q88. 집도둑
fixme. 당신은 전문털이범이다. 어느 집에서든 돈을 훔쳐올 수 있지만 경보 시스템 때문에
fixme. 바로 옆집은 훔칠 수 없고 한 칸 이상 떨어진 집만 가능하다.
fixme. 각 집에는 훔칠 수 있는 돈의 액수가 입력 값으로 표기되어 있다. 훔칠 수 있는 가장 큰 금액을 출력하라.
fixme. 입력 : [1, 2, 3, 1]
fixme. 출력 : 4
fixme. 설명
fixme. 첫 번째 집에서 1, 세번째 집에서 3, 따라서 1 + 3 = 4
fixme. 입력 : [2, 7, 9, 3, 1]
fixme. 출력 : 12
fixme. 설명
fixme. 첫 번째 집에서 2, 세 번째 집에서 9, 다섯 번째 집에서 1, 따라서 2 + 9 + 1 = 12이다.
"""

from typing import List
import collections

class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            return max(_rob(i - 1), _rob(i - 2) + nums[i])

        return _rob(len(nums) - 1)
    def robDP(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        print(dp)
        return dp.popitem()[1]

print(Solution().robDP([9,3,9,8]))