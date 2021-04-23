from sys import stdin
from typing import List
from collections import defaultdict, deque


class Solution:
    def slang(self, a: int, b: int, maps: List[List[int]]):
        graph = defaultdict(list)
        for u, v in maps:
            # 흠..같은거 걸러줘야함..
            if u == v:
                continue
            graph[u].append(v)
            graph[v].append(u)
        check = [-1] * 1001
        check[a] = 0
        queue = deque()
        queue.append(a)
        while queue:
            node = queue.popleft()
            if node == b:
                print(check[node])
                return
            for g in graph[node]:
                # 모두 -1 넣고 a에 0 삽입후 간 곳 업데이트하고 그럼 -1 아니니깐 또다시 없데이트 안되서 최소값이 들어가는 형태
                if check[g] == -1:
                    queue.append(g)
                    check[g] = check[node] + 1
        print(-1)
        return


a, b = map(int, stdin.readline().split())
N, M = map(int, stdin.readline().split())
tmp = []
for _ in range(M):
    tmp.append(list(map(int, stdin.readline().split())))
Solution().slang(a, b, tmp)
