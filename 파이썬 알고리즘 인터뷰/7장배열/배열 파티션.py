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
