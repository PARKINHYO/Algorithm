"""
fixme. https://leetcode.com/problems/single-number
fixme. Q70. 싱글 넘버
fixme. 딱 하나를 제외하고 모든 엘리먼트는 2개씩 있다. 1개인 엘리먼트를 찾아라.
fixme. 입력 : [2, 2, 1]
fixme. 출력 : 1
fixme. 입력 : [4, 1, 2, 1, 2]
fixme. 출력 : 4
"""


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num


        return result
