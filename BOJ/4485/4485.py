import sys
input = sys.stdin.readline
from typing import List
import heapq


class Solution: 
    def min_lost(self, N: int, cave: List[List[int]]):
        Q = [(cave[0][0],0,0)]
        x = [-1,1,0,0]
        y = [0,0,-1,1]
        visited = [[False]*126 for _ in range(126)]
        while Q:
            cost, popx, popy = heapq.heappop(Q)
            if popx == N-1 and popy == N-1:
                return cost
            if not visited[popx][popy]:
                visited[popx][popy] = True
                for i in range(4):
                    newx = popx + x[i]
                    newy = popy + y[i]
                    if 0<=newx<N and 0<=newy<N:
                        if not visited[newx][newy]:
                            heapq.heappush(Q,(cave[newx][newy]+cost,newx,newy))

count = 1
while True:
    N = int(input())
    if N == 0:
        break
    cave = []
    for i in range(1, N+1):
        cave.append(list(map(int, input().split())))
    answer = Solution().min_lost(N, cave)
    print(f'Problem {count}: {answer}')
    count += 1

