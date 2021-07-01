import sys, collections, heapq, copy
from typing import List, Tuple
input = sys.stdin.readline


class Solution:
    def min_cost(self, start: int, end: int, g: List[List[Tuple]]):
        Q = []
        heapq.heappush(Q, (0, start))
        
        # 경로 저장
        path = collections.defaultdict(list)
        
        # 비용
        dist = [sys.maxsize]*1001
        dist[start] = 0
        
        while Q:
            w, u = heapq.heappop(Q)
            
            # 드는 비용이 저장된 비용보다 더 큰 경우 continue로 넘긴다. 
            if dist[u] < w:
                continue
            
            # 현재 위치를 현재 path에 저장
            path[u].append(u)
            
            # 현재 위치가 끝이면
            if u == end:
                return (w, path[u])
            
            # 현재 위치에서 갈 수 있는곳 반복
            for v, weight in g[u]:
                
                """갈 수 있는곳까지 갈 때 비용 + 현재까지 총 비용 이렇게 더해서
                dist에 저장된 비용과 비교해서 더 작으면 if 안으로 들어감"""
                if dist[v] > weight + w:
                    
                    # dist 기존에 저장된 값보다 weight + w가 작으니깐 업데이트
                    dist[v] = weight + w
                    
                    # heap에 갈수 있는 위치까지 갈 때 총비용, 갈 수 있는 위치 저장
                    heapq.heappush(Q, (dist[v], v))
                    
                    # 현재 위치까지의 path를 갈수 있는 곳의 path에 복사
                    path[v] = copy.deepcopy(path[u])


n = int(input())
m = int(input())
g = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
start, end = map(int, input().split())
answers = Solution().min_cost(start, end, g)
print(answers[0])
print(len(answers[1]))
print(*answers[1])
