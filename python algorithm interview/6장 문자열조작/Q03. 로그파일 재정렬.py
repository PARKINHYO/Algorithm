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
