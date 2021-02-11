## 6장 문자열 조작 

```python
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
            if strs.popleft() != strs.pop():
                return False

        return True

    def isPalindromeSlicing(self, s: str) -> bool:
        s = s.lower()

        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^0-9a-z]', '', s, count=1)

        return s == s[::-1]
```
<br><br>

```python
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
```

<br><br>

```python
"""
fixme. https://leetcode.com/problems/reorder-data-in-log-files/
fixme. Q02. 로그파일 재정렬
fixme. 로그를 재정렬하라. 기준은 다음과 같다.
fixme. 1. 로그의 가장 앞 부분은 식별자다.
fixme. 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
fixme. 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
fixme. 4. 숫자 로그는 입력 순서대로 한다.

fixme. Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
fixme. Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
fixme. Explanation:
fixme. The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
fixme. The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

fixme. Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
fixme. Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
"""

from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        # 2개의 키를 람다 표현식으로 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits
```

<br><br>

```python
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
```

<br><br>

```python
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
```

<br><br>

```python
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
```