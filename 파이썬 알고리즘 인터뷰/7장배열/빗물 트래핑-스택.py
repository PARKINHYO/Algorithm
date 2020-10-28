from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                print(f'i : {i}')
                print(f'stack : {stack}')
                print(f'height[i] : {height[i]}')
                print(f'height[stack[-1] : {height[stack[-1]]}')
                top = stack.pop()
                print(f'top : {top}')

                if not len(stack):
                    print('break\n')
                    break

                distance = i - stack[-1] -1
                print(f'distance : {distance}')
                waters = min(height[i], height[stack[-1]]) - height[top]
                print(f'waters : {waters}')
                volume += distance*waters
                print(f'volume : {volume}')
                print()

            stack.append(i)

        return volume


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))



