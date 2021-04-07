from typing import List
from sys import stdin


class Solution:
    def minValue(self, K: int, coins: List[int]):
        coins.sort(reverse=True)
        count = 0
        for c in coins:
            if K >= c:
                count += (K // c)
                K %= c
        print(count)

N, K = map(int, stdin.readline().split())
coins = [int(stdin.readline()) for x in range(N)]
Solution().minValue(K, coins)
