import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^0-9a-z]', '', s, count=1)

        return s == s[::-1]

