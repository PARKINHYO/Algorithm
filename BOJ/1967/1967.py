import sys
import collections

input = sys.stdin.readline
        
graph = collections.defaultdict(list)
n = int(input())

# n이 1일 때는 간선이 없으므로 0을 출력하고 종료
if n == 1:
    print(0)
    exit(0)
    
# 리프노드 집합. 우선 정접을 다 넣어주고 입력 받으면서 u부분을 빼준다. 
leafs = {x for x in range(1, n+1)}

# 루트에서 리프노드까지 거리를 넣을 딕셔너리
root_to_leafs = collections.defaultdict(int)

"""
루트에서 리프노드까지 탐색하고, 
리프노드에서 루트 및 다른 리프노드까지 탐색해야되므로 
그래프를 양방향으로 만들어준다. 
"""
for i in range(n-1):
    u, v, w = map(int, input().split())
    leafs.discard(u)
    graph[u].append((v, w))
    graph[v].append((u, w))

"""
루트노드에서 리프토드까지 bfs로 탐색하여 
거리가 최대인 리프노드를 구한다. 
"""
Q = collections.deque([(1, 0)])
visited = [False] * (n+1)
while Q:
    node, weight = Q.popleft()
    if node in leafs and not visited[node]:
        root_to_leafs[node] = weight
    if not visited[node]:
        visited[node] = True
        for v, w in graph[node]:
            alt = w + weight
            Q.append((v, alt))

# 루트노드에서 리프노드까지 거리가 담긴 root_to_leafs에서 Counter로 최대 값을 뽑아낸다. 
start = collections.Counter(root_to_leafs).most_common()[0][0]

"""
리프노드에서 루트 및 또다른 리프노드까지 거리를 구해서 최대 값이 최대지름이된다. 
이 값들을 저장할 딕셔너리임.
"""
start_to_leafs = collections.defaultdict(int)

# 루트에서 리프노드들까지 거리중에 최대 값인 리프노드를 제거해준다. 앞에서 구한 start.
leafs.discard(start)

"""
리프에 루트인 1을 추가해준다. 왜냐하면 정점이 두개 간선이 하나일 경우에는 
리프에서 루트까지 경우의 수 1개가 그냥 정답으로 되기 때문.
"""
leafs.add(1)

# 최대 리프노드에서 루트 및 다른 리프노드까지 탐색해서 거리를 구하고 최대인 값을 print하면 정답.
Q.append((start, 0))
visited = [False] * (n+1)
while Q:
    node, weight = Q.popleft()
    if node in leafs and not visited[node]:
        start_to_leafs[node] = weight
    if not visited[node]:
        visited[node] = True
        for v, w in graph[node]:
            alt = w + weight
            Q.append((v, alt))
print(collections.Counter(start_to_leafs).most_common()[0][1])