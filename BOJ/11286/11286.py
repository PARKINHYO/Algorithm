from typing import List
import heapq
from sys import stdin

class Solution:
    def abstractHeap(self, xList: List[int]):
        heap = []
        for x in xList:
            if x == 0:
                if heap:
                    print(heapq.heappop(heap)[1])
                else:
                    print(0)
            else:
                heapq.heappush(heap, (abs(x), x))

xList = []
for i in range(int(stdin.readline())):
    xList.append(int(stdin.readline()))
Solution().abstractHeap(xList)