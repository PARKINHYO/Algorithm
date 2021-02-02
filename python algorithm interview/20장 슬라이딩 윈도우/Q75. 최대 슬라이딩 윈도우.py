"""
fixme. https://leetcode.com/problems/sliding-window-maximum/
fixme. Q75. 최대 슬라이딩 윈도우
fixme. 배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지
fixme. 이동하면서 최대 슬라이딩 윈도우를 구하라.
fixme. 입력 nums = [1,3,-1,-3,5,3,6,7], k = 3
fixme. 출력 [3,3,5,5,6,7]
fixme. 설명
fixme. 윈도우 포지션                           최대
fixme. ---------------------------------   ------
fixme. [1   3   -1]   -3   5   3   6   7     3
fixme. 1   [3   -1   -3]   5   3   6   7     3
fixme. 1   3   [-1   -3   5]   3   6   7     5
fixme. 1   3   -1   [-3   5   3]   6   7     5
fixme. 1   3   -1   -3   [5   3   6]   7     6
fixme. 1   3   -1   -3   5   [3   6   7]     7
"""

from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums

        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i+k]))

        return r

    def maxSlidingWindowQueue(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v


            results.append(current_max)

            # 최댓값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')

        return results