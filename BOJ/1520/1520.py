import sys, heapq
from typing import List
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


class Solution:
    def down_hill(self, M: int, N: int, graph: List[List[int]]):
        """dfs로 탐색을 하고 dp기법을 사용하여 배열에 각 칸마다의 
        결과 값을 저장해나가면서 이전에 갔었던 칸을 지나갈시에 
        dp에서 답을 가져와서 사용함으로써 깊이 탐색의 시간을 줄인다."""
        def dfs(x,y):
            
            # 도착 지점일시 1반환
            if x == M-1 and y == N-1:
                return 1
            
            """기본적으로 -1이 들어 있는데 -1아닌 경우 
            이미 방문한 곳임. 그 자리의 dp 값을 반환해버린다.
            """
            if dp[x][y] != -1:
                return dp[x][y]
            
            """상, 하, 좌, 우 가기전에 현재 좌표를 -1에서 0으로 
            바꾼다. 도착지점까지 갈 수 있을지 없을지 모르고, 
            방문은 했으니깐 0으로"""
            dp[x][y] = 0
            
            # 상, 하, 좌, 우
            for i in range(4):
                newx = x + grid_x[i]
                newy = y + grid_y[i]
                if 0<=newx<M and 0<=newy<N:
                    if graph[x][y] > graph[newx][newy]:
                        """상, 하, 좌, 우 중에서 현재 값보다 작은 경우 여기로 오게 되는데
                        그럴 경우마다 상, 하, 좌, 우 깊이 우선 탐색을 하고 
                        그 반환된 값을 현재의 dp로 저장. 밑에 사진을 보면 이해할 수 있다. """
                        dp[x][y] += dfs(newx,newy)
                        
            # 결국 dfs호출된게 다 반환되면서 dp[0][0]을 반환하게 된다.
            return dp[x][y]
        
        # 상, 하, 좌, 우 이동용 x, y 좌표
        grid_x = [0,0,-1,1]
        grid_y = [-1,1,0,0]
        
        # dp 배열 모든 곳에 -1 넣음.
        dp = [[-1]*N for _ in range(M)]
        return dfs(0,0) 

M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))
print(Solution().down_hill(M, N, graph))
