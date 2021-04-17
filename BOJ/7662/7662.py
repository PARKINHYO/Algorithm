from sys import stdin
from typing import List
import heapq


class Solution:
    def myPriorityQueue(self, data: List[List[str]]):
        minHeap = []
        maxHeap = []
        visited = [False] * 1000001
        for i in range(len(data)):
            if data[i][0] == "I":
                heapq.heappush(minHeap, (int(data[i][1]), i))
                heapq.heappush(maxHeap, (-int(data[i][1]), i))
                visited[i] = True
            else:
                if data[i][1] == '-1':
                    while minHeap and not visited[minHeap[0][1]]:
                        heapq.heappop(minHeap)
                    if minHeap:
                        visited[minHeap[0][1]] = False
                        heapq.heappop(minHeap)

                if data[i][1] == '1':
                    while maxHeap and not visited[maxHeap[0][1]]:
                        heapq.heappop(maxHeap)
                    if maxHeap:
                        visited[maxHeap[0][1]] = False
                        heapq.heappop(maxHeap)

        while minHeap and not visited[minHeap[0][1]]:
            heapq.heappop(minHeap)
        while maxHeap and not visited[maxHeap[0][1]]:
            heapq.heappop(maxHeap)
        if minHeap and maxHeap:
            print(maxHeap[0][0] * -1, minHeap[0][0])
        else:
            print('EMPTY')


for _ in range(int(stdin.readline())):
    data = []
    for _ in range(int(stdin.readline())):
        data.append(list(stdin.readline().split()))
    Solution().myPriorityQueue(data)
