from typing import List
from sys import stdin
import heapq


class Solution:
    def cardCombine(self, n: int, m: int, cards: List[int]):
        heap = cards[:]
        heapq.heapify(heap)
        for _ in range(m):
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            tmp = x + y
            heapq.heappush(heap, tmp)
            heapq.heappush(heap, tmp)
        print(sum(heap))

n, m = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))
Solution().cardCombine(n, m, cards)
