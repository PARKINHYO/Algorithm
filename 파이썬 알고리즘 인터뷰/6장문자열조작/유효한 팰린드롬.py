
import collections
from typing import Deque
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^0-9a-z]', '', s)

        return s == s[::-1]


e

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))





# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#
#         strs: Deque = collections.deque()
#
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
#
#         return True
#
#
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#
#         # 펠린드롬 여부 판별
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#
#         return True


