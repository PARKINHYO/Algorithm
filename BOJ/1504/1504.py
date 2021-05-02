import sys
import collections
import heapq

N, E = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
A, B = map(int, sys.stdin.readline().split())

route = [[1, A, B, N], [1, B, A, N]]
answers = []
for i in range(2):
    roads = 0
    for j in range(len(route[0])-1):
        Q = [(0, route[i][j])]
        visited = [False] * 801
        while Q:
            weight, u = heapq.heappop(Q)
            visited[u] = True
            if u == route[i][j+1]:
                roads += weight
                break
            for v in graph[u]:
                if not visited[v[0]]:
                    tmp = v[1] + weight
                    heapq.heappush(Q, (tmp, v[0]))
        
        if roads == 0:
            break
    answers.append(roads)
if not answers:
    print(-1)
else:
    print(min(answers))
