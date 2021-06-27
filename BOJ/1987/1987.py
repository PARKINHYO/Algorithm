import collections
from typing import List
import sys
input = sys.stdin.readline


class Solution:
    def alphabet(self, R: int, C: int, board: List):
        """bfs를 탐색하기 위해 큐를 만드는데 
        set자료형으로 같은것을 없애야지 시간을 단축할 수 있음
        예를 들면 IEHFALKC는 IEHF쪽에서 2가지의 경우로 A를 갈 수 있으므로
        이런 경우 다 set으로 없애준다."""
        
        # 큐에서 원소는 순서대로 x좌표, y좌표, 지금까지거쳐간 알파벳들
        Q = set([(0, 0, board[0][0])])
        
        # x, y 위, 아래, 왼쪽, 오른쪽
        gridx = [-1, 0, 1, 0]
        gridy = [0, -1, 0, 1]
        
        answer = 1
        while Q:
            x, y, alphabets = Q.pop()

            # 상하좌우 for문
            for i in range(4):
                newx = x + gridx[i]
                newy = y + gridy[i]
                # 새로운 좌표가 행렬 인덱스 범위 안쪽에 있을 떄
                if 0 <= newx < R and 0 <= newy < C:
                    
                    # 새로운 좌표에 있는 알파벳이 현재까지 거쳐간 알파벳들중에 없을 때
                    if board[newx][newy] not in alphabets:
                        
                        Q.add((newx, newy, alphabets+board[newx][newy]))
                        """위에서 지금까지 거쳐간 알파벳들에서 새롭게 찾은 알파벳을 더하므로 
                        len(alphabets)+1로 최댓값 찾는다."""
                        answer = max(answer, len(alphabets)+1)  
        return answer


R, C = map(int, input().split())
print(Solution().alphabet(R, C, [input().rstrip() for _ in range(R)]))
