from sys import stdin
from typing import List
from collections import defaultdict, deque


class Solution:
    def findCity(self, N: int, M: int, K: int, X: int, map: List[List[int]]):
        graph = defaultdict(list)
        for a, b in map:
            graph[a].append(b)
        count = 0
        queue = deque([[X, count]])
        visited = [False] * 300001
        visited[X] = True
        answer = []
        while queue:
            u, count = queue.popleft()
            if count == K:
                answer.append(u)

            for v in graph[u]:
                if not visited[v]:
                    queue.append([v, count + 1])
                    visited[v] = True

        if not answer:
            print(-1)
        else:
            answer.sort()
            for i in answer:
                print(i)


N, M, K, X = map(int, stdin.readline().split())
graph = []
for i in range(M):
    graph.append(list(map(int, stdin.readline().split())))
Solution().findCity(N, M, K, X, graph)
