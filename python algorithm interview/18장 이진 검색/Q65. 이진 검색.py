from typing import List
import bisect


class Solution:
    def search_recursive(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2
                print(mid)
                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid

            else:
                return -1

        return binary_search(0, len(nums) - 1)

    def search_while(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    def search_bisect(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    def search_index(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


print(Solution().search_recursive([1,2], 2))