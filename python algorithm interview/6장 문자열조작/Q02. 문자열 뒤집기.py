"""
fixme. https://leetcode.com/problems/reverse-string
fixme. Q02. 문자열 뒤집기
fixme. 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
fixme. Input: ["h","e","l","l","o"]
fixme. Output: ["o","l","l","e","h"]
fixme. Input: ["H","a","n","n","a","h"]
fixme. Output: ["h","a","n","n","a","H"]
"""

from typing import List


class Solution:
    def reverseStringTwoPointer(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseStringPython(self, s: List[str]) -> None:
        s.reverse()
