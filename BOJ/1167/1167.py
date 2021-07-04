from typing import List, Tuple
import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


class Solution: 
    def diameter(self, V: int, graph: List[List[Tuple]]):
        def dfs(u, count):
            visited[u] = True
            for v, w in graph[u]:
                if not visited[v]:
                    vertex, weight = dfs(v, count+w)
                    if weight > answer[1]:
                        answer[0], answer[1] = vertex, weight
            return (u, count)

        # 정점과 거리 누적 값을 저장
        answer = [0, 0]
        
        visited = [False] * (V+1)

        # 아무 정점에서 dfs를 돌려서 최대 거리인 곳의 정점을 구한다
        dfs(1, 0)

        start = answer[0]
        
        # 정점과 거리 누적 값을 저장
        answer = [0, 0]
        
        visited = [False] * (V+1)

        # 최대 거리인 정점에서 다시 dfs를 돌려서 최대 거리를 구하면 지름의 최댓값
        dfs(start, 0)

        return answer[1]


graph = collections.defaultdict(list)
V = int(input())
for _ in range(V):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-1, 2):
        graph[tmp[0]].append((tmp[i], tmp[i+1]))
print(Solution().diameter(V, graph))
