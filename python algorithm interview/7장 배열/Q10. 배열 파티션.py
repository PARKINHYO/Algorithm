"""
fixme. https://leetcode.com/problems/array-partition-i/
fixme. Q10. 배열 파티션Ⅰ
fixme. n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라 .
fixme. Input: nums = [1,4,3,2]
fixme. Output: 4
fixme. Explanation: All possible pairings (ignoring the ordering of elements) are:
fixme. 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
fixme. 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
fixme. 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
fixme. So the maximum possible sum is 4.
"""

from typing import List


class Solution:
    def arrayPairSum1(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

    def arrayPairSum2(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n

        return sum

    def arrayPairSum3(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
