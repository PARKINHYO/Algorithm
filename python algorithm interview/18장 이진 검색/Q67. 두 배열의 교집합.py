"""
fixme. https://leetcode.com/problems/intersection-of-two-arrays/
fixme. Q67. 두 배열의 교집합
fixme. 두 배열의 교집합을 구하라.
fixme. 입력 : nums1 = [1,2,2,1], nums2 = [2,2]
fixme. 출력 : 2
fixme. 입력 : nums1 = [4,9,5], nums2 = [9,4,9,8,4]
fixme. 출력 : [9, 4]
"""

from typing import List, Set
import bisect


class Solution:
    def intersection_bruteforce(self, num1: List[int], num2: List[int]) -> Set:
        result: Set = set()
        for n1 in num1:
            for n2 in num2:
                if n1 == n2:
                    result.add(n1)

        return result

    def intersection_bin_search(self, nums1: List[int], nums2: List[int]) -> Set:
        result: Set = set()
        nums2.sort()
        for n1 in nums1:
            # 이진 검색으로 일치 여부 판별, bisect_left는 들어갈 위치를 왼쪽 기준으로 반환
            i2 = bisect.bisect_left(nums2, n1)
            print(i2)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)

        return result

    def intersection_pointer(self, nums1: List[int], nums2: List[int]) -> Set:
        result: Set = set()
        nums1.sort()
        nums2.sort()
        i = j = 0
        # 투 포인터 우측으로 이동하여 일치 여부 판별
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                j += 1
                i += 1

        return result



Solution().intersection_bin_search([1, 2, 2, 1], [2, 2])
