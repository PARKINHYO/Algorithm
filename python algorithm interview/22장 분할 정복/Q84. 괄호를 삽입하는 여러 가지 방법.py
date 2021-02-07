"""
fixme. https://leetcode.com/problems/different-ways-to-add-parentheses/
fixme. Q84. 괄호를 삽입하는 여러 가지 방법
fixme. 숫자와 연산자를 입력 받아 가능한 모든 조합의 결과를 출력하라
fixme. 입력 : "2-1-1"
fixme. 출력 : [0, 2]
fixme. 설명
fixme. ((2-1)-1) = 0
fixme. (2-(1-1)) = 2

fixme. 입력 : "2*3-4*5"
fixme. 출력 : [-34, -14, -10, -10, 10]
fixme. 설명
fixme. (2*(3-(4*5))) = -34
fixme. ((2*3)-(4*5)) = -14
fixme. ((2*(3-4))*5) = -10
fixme. (2*((3-4)*5)) = -10
fixme. (((2*3)-4)*5) = 10
"""

from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])
                print(left, right, value)
                results.extend(compute(left, right, value))
                print(results)
        return results


print(Solution().diffWaysToCompute("2*3-4*5"))
