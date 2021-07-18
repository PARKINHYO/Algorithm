import sys
import collections
from typing import List
input = sys.stdin.readline


class Solution:
    def ACM_craft(self, N: int, K: int, time: List[int],
                  graph: List[List[int]], degree: List[int], W: int):
        
        dp = [0]*(N+1) # 각 건물마다 완료 시간 넣는 dp
        
        q = collections.deque()
        
        for i in range(1, N+1):
            
            # 진입 차수가 0이면 데크에 다 넣고, dp에 해당 건물 건설 시간 넣음
            if degree[i] == 0:
                q.append(i)
                dp[i] += time[i]
                
        """큐에서 하나씩 빼면서 그래프 돔
        그 때마다 차수를 하나씩 빼주고 
        dp는 pop_node dp 값이랑 
        그래프 돌면서 나오는 정점의 건물 건설 시간이랑 더한다음 
        기존 dp랑 비교해서 max 값 삽입"""
        while q:
            pop_node = q.popleft()
            for i in graph[pop_node]:
                degree[i] -= 1
                dp[i] = max(dp[i], dp[pop_node] + time[i])
                if degree[i] == 0:
                    q.append(i)
        return dp[W]


for _ in range(int(input())):
    
    # 건물의 개수, 건물간의 건설순서 규칙
    N, K = map(int, input().split())
    
    """각 건물당 건설에 걸리는 시간 0은 아에 없어서 
    0으로 두고 인덱스 1부터 넣음."""
    time = [0] + list(map(int, input().split()))
    
    graph = collections.defaultdict(list)
    
    degree = [0]*(N+1) # 진입 차수
    
    for _ in range(K):
        u, v = map(int, input().split())
        graph[u].append(v) 
        degree[v] += 1 # v, 진입 차수 1 증가
        
    W = int(input()) # 마지막 건설 건물 번호
    
    print(Solution().ACM_craft(N, K, time, graph, degree, W))
    