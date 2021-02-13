"""
fixme. https://leetcode.com/problems/product-of-array-except-self/
fixme. Q11. 자신을 제외한 배열의 곱
fixme. 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셉 결과가 되도록 출력하라.
fixme. Input:  [1,2,3,4]
fixme. Output: [24,12,8,6]
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1

        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1

        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return out
