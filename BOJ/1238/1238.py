import sys
import collections
import heapq

def dijkstra(start, dp, graph):
    Q = [(0, start)]
    dp[start] = 0
    while Q:
        weight, u = heapq.heappop(Q)
        if dp[n] < weight:
            continue
        for v, w  in graph[u]:
            alt = weight + w
            if alt < dp[v]:
                dp[v] = alt
                heapq.heappush(Q, (alt, v))
            

N, M, X = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
# 1~N까지 출발지에서 도착지 X까지 가야되는데 이걸 꺼꾸로 생각해서, 도착지 X에서 각 출발지로 가는 그래프를 위해서 역방향으로 그래프를 만든다.
oppsite_graph = collections.defaultdict(list)

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    oppsite_graph[v].append((u, w))


# 출발지에서 도착지, 도착지에서 출발지까지 갈 dp를 선언. 이러면 다익스트라 2번만 돌리면 된다. 
dp = [sys.maxsize]*(N+1)
oppsite_dp = [sys.maxsize]*(N+1)

# 출발지에서 도착지
dijkstra(X, oppsite_dp, oppsite_graph)

# 도착지에서 출발지
dijkstra(X, dp, graph)

answer = 0
for i in range(1, N+1):
    answer = max(answer, dp[i] + oppsite_dp[i])
print(answer)

