from typing import List
import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k:int):
            if k == 0:
                results.append(elements[:])

            for i in range(start, n+1):
                elements.append(i)
                print(f'range({start},{n+1}), elements: {elements}, dfs({i+1}, {k-1})')
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([], 1, k)
        return results

Solution().combine(4,2)