"""
fixme. https://leetcode.com/problems/trapping-rain-water/
fixme. Q08. 빗물 트래핑
fixme. 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

fixme. Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
fixme. Output: 6
fixme. Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
fixme. In this case, 6 units of rain water (blue section) are being trapped.

fixme. Input: height = [4,2,0,3,2,5]
fixme. Output: 9
"""

from typing import List


class Solution:
    def trapTwoPointer(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

    def trapStack(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                print(i)
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters

            stack.append(i)
        print(stack)
        return volume


Solution().trapStack([0,1,0,2,1,0,1,3,2,1,2,1])