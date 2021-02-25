from typing import List
import collections
from sys import stdin


class Solution:
    def numberCard2(self, N: int, cards: List[int], M: int, problems: List[int]) -> List[int]:
        answer = []
        counter = collections.Counter(cards)
        for problem in problems:
            if problem in counter:
                answer.append(counter[problem])
            else:
                answer.append(0)

        return answer


N = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
problems = list(map(int, stdin.readline().split()))
print(*Solution().numberCard2(N, cards, M, problems))
