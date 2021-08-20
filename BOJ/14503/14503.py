import sys
from typing import List
input = sys.stdin.readline


class Solution:
    def vacuum_cleaner(self, N: int, M: int, r: int,
                       c: int, d: int, board: List[List[int]]):
        
        """북, 동, 남, 서 순으로 d가 0, 1, 2, 3 이므로
        이걸 인덱스로 해서 x, y 좌표를 만든다."""
        x, y = (-1, 0, 1, 0), (0, 1, 0, -1)
        
        """빈칸이면 0, 벽이면 1, 청소했으면 2"""
        board[r][c] = 2 # 처음 값을 청소한 걸로
        
        answer = 1
        while True:
            check = False
            for _ in range(4): # 4번 회전을 위한 for문
                
                """북이면 서, 동이면 북과 같이 왼쪽 회전해야 되므로,
                x, y좌표의 인덱스로 사용하고 있는 d를 오른쪽으로 3칸 
                이동시킨다."""
                rotated_d = (d+3) % 4
                new_x, new_y = r + x[rotated_d], c + y[rotated_d]
                d = rotated_d
                
                # 만약 board[new_x][new_y]가 0이면 청소 가능
                if 0 <= new_x < N and 0 <= new_y < M and \
                    not board[new_x][new_y]:
                    board[new_x][new_y] = 2
                    answer += 1
                    r, c = new_x, new_y
                    check = True
                    break
            
            # 4번의 회전 중 청소 가능한 곳이 아에 없을 떄
            if not check:
                
                """북이면 남, 동이면 서로 반대 방향으로 이동하는 것이므로
                기존 d를 인덱스로한 좌표를 더하지 않고 빼준다."""
                if board[r-x[d]][c-y[d]] == 1:
                    return answer
                else:
                    r, c = r-x[d], c-y[d]
                    

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(Solution().vacuum_cleaner(N, M, r, c, d, board))
