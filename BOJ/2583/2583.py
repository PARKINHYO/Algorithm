from sys import stdin
from typing import List
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def findArea(self, M: int, N: int, graph: List[List[int]]):
        def dfs(i, j):
            if i < 0 or i >= M or j < 0 or j >= N or graph[i][j] != 0:
                return

            graph[i][j] = 1
            tmp[0] += 1
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        area = []
        tmp = [0]
        count = 0
        for i in range(M):
            for j in range(N):
                if graph[i][j] == 0:
                    count += 1
                    dfs(i, j)
                    area.append(tmp[0])
                    tmp[0] = 0
        print(count)
        area.sort()
        print(*area)


M, N, K = map(int, stdin.readline().split())
graph = [[0] * N for i in range(M)]
for i in range(K):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            graph[j][k] = 1

Solution().findArea(M, N, graph)
