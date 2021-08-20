import sys
import collections
from typing import List
input = sys.stdin.readline


class Solution:
    def make_maze(self, n: int, graph: List[str]):
        queue = collections.deque([(0, 0, 0)])
        visited = [[False]*n for _ in range(n)]
        grid_x = [0, 0, 1, -1]
        grid_y = [1, -1, 0, 0]
        while queue:
            x, y, count = queue.popleft()
            if x == n-1 and y == n-1:
                return count
            if not visited[x][y]:
                visited[x][y] = True
                for i in range(4):
                    new_x = x + grid_x[i]
                    new_y = y + grid_y[i]
                    if 0 <= new_x < n and 0 <= new_y < n and graph[new_x][new_y] == '1':
                        queue.appendleft((new_x, new_y, count))
                    elif 0 <= new_x < n and 0 <= new_y < n and graph[new_x][new_y] == '0':
                        queue.append((new_x, new_y, count+1))


n = int(input())
print(Solution().make_maze(n, [input().rstrip() for _ in range(n)]))
