"""
fixme. https://leetcode.com/problems/search-in-rotated-sorted-array/
fixme. Q66. 회전 정렬된 배열 검색
fixme. 특정 피벗을 기준으로 회전하여 정렬된 배열에서 target 값의 인덱스를 출력하라.
fixme. 입력 : nums = [4,5,6,7,0,1,2], target = 1
fixme. 출력 : 출력 1
fixme. 정렬된 입력값은 [0,1,2,3,4,5,6,7]이며 여기서 이진 검색을 통해 1의 위치를 찾은 다음(위치 1)
fixme. 원래의 입력값에서 얼마만큼 돌아가 있는지를 확인하여(4칸), '위치 1 + 4칸 = 인덱스 5'를 리턴.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 예외처리
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 피벗 기준 이진 검색
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1