from sys import stdin
import heapq
from collections import defaultdict


class Solution:
    def minimalCost(self, start: int, end: int, graph):
        heap = []
        heapq.heappush(heap, (0, start))
        dist = [False] * 1005
        while heap:
            w, u = heapq.heappop(heap)
            if dist[u] is False:
                dist[u] = w
                for v, tmp in graph[u]:
                    heapq.heappush(heap, (w + tmp, v))
        print(dist[end])


graph = defaultdict(list)
N = int(stdin.readline())
M = int(stdin.readline())
for i in range(M):
    u, v, w = map(int, stdin.readline().split())
    graph[u].append((v, w))
start, end = map(int, stdin.readline().split())
Solution().minimalCost(start, end, graph)
