"""
fixme. https://leetcode.com/problems/maximum-subarray/
fixme. Q86. 합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라.
fixme. 입력 : [-2, 1, -3, 4, -1, 2, 1, -5, 4]
fixme. 출력 : 6
fixme. 설명
fixme. [4, -1, 2, 1]은 합 6으로 가장 큰 서브 배열이다.
"""

from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)

    def maxSubArrayKadane(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)

        return best_sum