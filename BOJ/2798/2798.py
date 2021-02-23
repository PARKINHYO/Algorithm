from typing import List


class Solution:
    def blackJack(self, N: int, M: int, cards: List[int]) -> int:
        sums = []
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if cards[i] + cards[j] + cards[k] <= M:
                        sums.append(cards[i] + cards[j] + cards[k])
        return max(sums)


N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(Solution().blackJack(N, M, cards))
