"""
fixme. https://leetcode.com/problems/valid-palindrome/
fixme. Q01. 유효한 팰린드롬
fixme. 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
fixme. 입력 : "A man, a plan, a canal: Panama"
fixme. 출력 : true
fixme. 입력 : "race a car"
fixme. 출력 : false
"""

from typing import Deque
import collections
import re


class Solution:
    def isPalindromeList(self, s: str) -> bool:
        strs = []

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 펠린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

    def isPalindromeDeque(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():li

        return True

    def isPalindromeSlicing(self, s: str) -> bool:
        s = s.lower()

        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^0-9a-z]', '', s, count=1)

        return s == s[::-1]
