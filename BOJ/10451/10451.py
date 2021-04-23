from sys import stdin
from typing import List
from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    def permutationCycle(self, N: int, L: List[int]):
        def dfs(i):

            visited[i] = True

            for g in graph[i]:
                if not visited[g]:
                    dfs(g)

        graph = defaultdict(list)
        for i in range(N):
            graph[i + 1].append(L[i])
        visited = [False] * 1001
        count = 0
        for i in range(1, N + 1):
            if not visited[i]:
                count += 1
                dfs(i)
        print(count)


for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    Solution().permutationCycle(N, list(map(int, stdin.readline().split())))
