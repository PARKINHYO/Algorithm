import sys
import heapq
import sys

N = int(sys.stdin.readline())
classTime = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
classTime.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue, classTime[0][1])

for i in range(1, N):
    if queue[0] > classTime[i][0]:
        heapq.heappush(queue, classTime[i][1])
    else:
        heapq.heappop(queue)
        heapq.heappush(queue, classTime[i][1])
print(len(queue))