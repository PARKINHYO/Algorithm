"""
fixme. https://leetcode.com/problems/longest-palindromic-substring/
fixme. Q06. 가장 긴 팰린드롬 부분 문자열
fixme. 가장 긴 팰린드롬 부분 문자열을 출력하라.

fixme. Input: s = "babad"
fixme. Output: "bab" or "aba"

fixme.Input: s = "cbbd"
fixme. Output: "bb"

fixme. Input: s = "a"
fixme. Output: "a"

fixme. Input: s = "ac"
fixme. Output: "a"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result


