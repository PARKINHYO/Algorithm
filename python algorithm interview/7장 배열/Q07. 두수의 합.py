"""
fixme. https://leetcode.com/problems/two-sum/
fixme. 뎃셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

fixme. Input: nums = [2,7,11,15], target = 9
fixme. Output: [0,1]
fixme. Output: BecaInput: nums = [3,2,4], target = 6

fixme. Input: nums = [3,2,4], target = 6
fixme. Output: [1,2]

fixme. Input: nums = [3,3], target = 6
fixme. Output: [0,1]
"""

from typing import List


class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumIn(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

    def twoSumDictionary(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타멧에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [nums.index(num), nums_map[target - num]]

    def twoSumDictionaryFast(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        # 키와 값을 바꿔서 딕셔너리 저장.
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
