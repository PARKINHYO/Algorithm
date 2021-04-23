from sys import stdin
from typing import List
import sys
sys.setrecursionlimit(10**6)


class Solution:
    def quardTree(self, N: int, Map: List[List[str]]):
        def cur(x1, y1, x2, y2, n):
            if n == 1:
                return Map[y1][x1]
            mid = n // 2
            
            r1 = cur(x1, y1, x1+mid, y1+mid, mid)
            r2 = cur(x1+mid, y1, x1+n, y1+mid, mid)
            r3 = cur(x1, y1+mid, x1+mid, y1+n, mid)
            r4 = cur(x1+mid, y1+mid, x1+n, y1+n, mid)

            if r1 == r2 == r3 == r4 and len(r1)==1:
                return r1

            return "(" + r1 + r2 + r3 + r4 + ")"
        print(cur(0, 0, N, N, N))
        return


N = int(stdin.readline())
Map = [['0' for x in range(N)]for x in range(N)]
for i in range(N):
    line = input()
    for j in range(N):
        if line[j] == '1':
            Map[i][j] = line[j]

Solution().quardTree(N, Map)
