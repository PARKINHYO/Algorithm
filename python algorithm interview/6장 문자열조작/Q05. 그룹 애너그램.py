"""
fixme. https://leetcode.com/problems/group-anagrams/
fixme. Q49. 그룹 애너그램
fixme. 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
fixme. Input: strs = ["eat","tea","tan","ate","nat","bat"]
fixme. Output
fixme. [
fixme.     ["bat"],
fixme.     ["nat","tan"],
fixme.     ["ate","eat","tea"]
fixme. ]
"""

from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
