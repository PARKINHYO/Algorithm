from typing import List
from sys import stdin
import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    def numIslands(self, w: int, h: int, grid: List[List[int]]):
        def dfs(i, j):
            if i < 0 or i >= h or j < 0 or j >= w or grid[i][j] != 1:
                return

            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i - 1, j - 1)
            dfs(i + 1, j - 1)
            dfs(i - 1, j + 1)
            dfs(i + 1, j + 1)

        count = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    dfs(i, j)
                    count += 1
        print(count)


while True:
    grid = []
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    else:
        for i in range(h):
            grid.append(list(map(int, stdin.readline().split())))
        Solution().numIslands(w, h, grid)
