"""
fixme. https://leetcode.com/problems/majority-element/
fixme. Q83. 과반수 엘리먼트
fixme. 과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라.
fixme. 입력 : [3,2,3]
fixme. 출력 : 3
fixme. 입력 : [2,2,1,1,1,2,2]
fixme. 출력 : 2
"""
from typing import List
import collections

class Solution:
    # DP
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num

    # 분할 정복
    def majorityElement2(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement2(nums[:half])
        b = self.majorityElement2(nums[half:])

        return [b, a][nums.count(a) > half]


    def majorityElement3(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


print(Solution().majorityElement3([2,2,2,3,4,4,4]))