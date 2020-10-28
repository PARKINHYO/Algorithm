from typing import List
import re
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = defaultdict(int)

        for word in words:
            counts[word] +=1

        return max(counts, key=counts.get)

if __name__ == '__main__':
    s = Solution()
    print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))