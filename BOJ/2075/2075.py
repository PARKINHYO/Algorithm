import sys
import heapq

N = int(sys.stdin.readline())

nxn = []
for _ in range(N):
    nxn.extend(list(map(int, sys.stdin.readline().split())))
    

for _ in range(N*N-N):
    heapq.heappop(nxn)
    
print(heapq.heappop(nxn))