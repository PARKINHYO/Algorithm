"""
fixme. https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
fixme. Q68. 두수의 합Ⅱ
fixme. 정렬된 배열을 받아 덧셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
fixme. 주의: 이문제에서 배열은 0이 아닌 1부터 시작하는 것으로 한다.
fixme. 입력: numbers = [2,7,11,15], target = 9
fixme. 출력: [1,2]
"""

from typing import List
import bisect


class Solution:
    def twoSum_pointer(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]

    def twoSum_bin_search(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            # 이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return [k + 1, mid + 1]

    def twoSum_bisect(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k+1)
            if i < len(numbers) and numbers[i] == expected:
                return [k + 1, i + 1]

