from sys import stdin
from typing import List
from collections import deque
import heapq


class Solution:
    def algoSpot(self, M: int, N: int, m: List[List[str]]):

        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        queue = [(0, 0, 0)]
        visited = [[False] * (M + 1) for x in range(N + 1)]
        while queue:
            dist, popX, popY = heapq.heappop(queue)
            if popX == M - 1 and popY == N - 1:
                print(dist)
                return
            if not visited[popY][popX]:
                visited[popY][popX] = True
                if m[popY][popX] == '1':
                    dist += 1
                for i in range(4):
                    appendX = popX + x[i]
                    appendY = popY + y[i]
                    if 0 <= appendX < M and 0 <= appendY < N:
                        heapq.heappush(queue, (dist, appendX, appendY))

        return


M, N = map(int, stdin.readline().split())
m = []
for _ in range(N):
    string = input()
    tmp = []
    for char in string:
        tmp.append(char)
    m.append(tmp)

Solution().algoSpot(M, N, m)
