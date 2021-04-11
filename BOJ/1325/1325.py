from typing import List
from collections import defaultdict, deque
from sys import stdin


class Solution:
    def hacking(self, N: int, L: List[List[int]]):
        graph = defaultdict(list)

        # 그래프 만들기. 반대로 넣어줌.
        for v, u in L:
            graph[u].append(v)
        answer = 0
        answer_list = []

        # 정점을 싹다 돌면서 BFS로 탐색해줌. count 변수로 몇개 탐색됐나 새줌.
        for i in range(1, N + 1):
            queue = deque([i])
            visited = [False] * 10001
            visited[i] = True
            count = 1
            while queue:
                number = queue.pop()
                for v in graph[number]:
                    if not visited[v]:
                        queue.append(v)
                        visited[v] = True
                        count += 1

            # answer_list에 count가 가장 많은 것만 담음
            if answer < count:
                answer = countㅋ
                answer_list = [i]
            elif answer == count:
                answer_list.append(i)
        print(*answer_list)


N, M = map(int, stdin.readline().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, stdin.readline().split())))
Solution().hacking(N, graph)
