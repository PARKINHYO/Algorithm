from typing import List

class Soluton():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            nums_map[num] = i

        print(nums_map)

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [nums.index(num), nums_map[target-num]]