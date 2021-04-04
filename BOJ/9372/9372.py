from typing import List
from collections import defaultdict
from sys import stdin


class Solution:

    def travel(self, N: int, M: int, graph: List[List[int]]):
        def dfs(u):
            visited[u] = True
            if not myGraph[u]:
                return
            for g in myGraph[u]:
                if not visited[g]:
                    answer[0] += 1
                    dfs(g)

        answer = [0]
        visited = [False]*1001
        myGraph = defaultdict(list)
        for g in graph:
            myGraph[g[0]].append(g[1])
            myGraph[g[1]].append(g[0])
        dfs(1)
        print(answer[0])



for _ in range(int(stdin.readline())):
    N, M = map(int, input().split())
    graph = []
    for _ in range(M):
       graph.append(list(map(int, stdin.readline().split())))

    Solution().travel(N, M, graph)