"""
fixme.
 https://leetcode.com/problems/valid-parentheses/
 Q20. 유효한 괄호
 괄호로 된 입력값이 올바른지 판별하라.
 입력 : ()[]{}
 출력 : true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {')' : '(', '}': '{', ']': '['}

        for char in s:
            if char not in table:
                stack.append(char)
                print(stack)
            elif not stack or table[char] != stack.pop():
                return False
        print(stack)
        return len(stack) == 0

Solution().isValid('()[]{}')


