from typing import List
import sys
input = sys.stdin.readline
import sys
from collections import deque


class Solution:
    def breakWall(self, N: int, M: int, G: List[str]):
        # 상, 하, 좌, 우 좌표
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]
        
        # 큐안에 x좌표, y좌표, 벽을 뚤었나 0 안뚤었나1을 담음.
        Q = deque([(0,0,1)])
        
        """x, y좌표 각각마다 [0,0]을 만들고, 
        벽을 이미 한번 뚤었으면 인덱스 0, 벽을 아직 안뚤었으며 인덱스 1임.
        왜냐하면 위의 큐 마지막원소로 벽을 뚤었냐 안뚤었나로 0, 1을 넣고 
        이걸 visited[x][y][0], visited[x][y][1] 같은 방식으로 사용함."""
        visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
        
        """처음 시작점 0, 0에 첫 시작이니 벽이 안뚤려서 인덱스가 1이므로 
        visited[0][0][1] = 1로 총 방문 한번 한걸로 설정하고 큐로 들어간다.
        visited에 총 방문한곳의 개수가 계속 쌓인다."""
        visited[0][0][1] = 1
        
        while Q:
            
            # x좌표, y좌표, popv: 1이면 벽 뚤기 가능, 0이면 벽못뚤음
            popx, popy, popv = Q.popleft()
            
            # 목적지 도착시 visited를 반환하면 정답
            if popx == N-1 and popy == M-1:
                return visited[popx][popy][popv]
            
            # 상, 하, 좌, 우 돌리기
            for i in range(4):
                newx = popx + x[i]
                newy = popy + y[i]
                
                # 행렬 범위 안에 있고, 방문 안한 경우
                if 0<=newx<N and 0<=newy<M and visited[newx][newy][popv] == 0:
                    
                    # 벽이 등장하고, popv가 1 즉, 벽 뚤을 수 있음
                    if G[newx][newy] == '1' and popv == 1:
                        
                        """visited[popx][popy][popv] -> 현재 방문한 횟수에 1을 더한 값을 
                        옮겨간 좌표+인덱스 0으로 바꾼곳에 넣어줌"""
                        visited[newx][newy][0] = visited[popx][popy][popv] + 1
                        
                        """새로운 좌표 + 인덱스 0(벽못뚤음)으로 큐에 추가. 
                        왜냐면 지금 벽 뚤어서 이제 못뚤음"""
                        Q.append((newx, newy, 0))
                    
                    # 그냥 갈수 있는길
                    elif G[newx][newy] == '0':
                        
                        # 벽을 뚤지 않았으니깐 새로운 좌표 popv에 그대로 전꺼 1더한 값을 넣어줌
                        visited[newx][newy][popv] = visited[popx][popy][popv] + 1
                        
                        # 벽을 뚤지 않았으니깐 이전값 popv 그대로 넣어줌
                        Q.append((newx,newy,popv))
        return -1


N, M = map(int, input().split())
print(Solution().breakWall(N, M, [input().rstrip() for _ in range(N)]))
