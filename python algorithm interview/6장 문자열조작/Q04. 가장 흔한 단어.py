"""
fixme. https://leetcode.com/problems/most-common-word/
fixme. Q04. 가장 흔한 단어
fixme. 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며,
fixme. 구두점(마침표, 쉼표 등) 또한 무시한다.
fixme. Input
fixme. paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
fixme. banned = ["hit"]
fixme. Output: "ball"
fixme. Explanation
fixme. "hit" occurs 3 times, but it is a banned word.
fixme. "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
fixme. Note that words in the paragraph are not case sensitive,
fixme. that punctuation is ignored (even if adjacent to words, such as "ball,"),
fixme. and that "hit" isn't the answer even though it occurs more because it is banned.
"""

from typing import List
import re
import collections


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
            .lower().split()
                 if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]
