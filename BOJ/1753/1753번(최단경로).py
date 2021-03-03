import collections
import heapq
from sys import stdin


class Solution:
    def shortestPath(self, V: int, E: int, K: int, graph: dict):
        dist = collections.defaultdict(int)
        q = [[0, K]]
        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = w + time
                    heapq.heappush(q, (alt, v))
        for i in range(V):
            if i + 1 in dist:
                print(dist[i + 1])
            else:
                print("INF")


graph = collections.defaultdict(list)
V, E = map(int, stdin.readline().split())
K = int(stdin.readline())
for i in range(E):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))

Solution().shortestPath(V, E, K, graph)