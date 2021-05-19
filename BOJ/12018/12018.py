import sys
import heapq


n, m = map(int, sys.stdin.readline().split())
candidates = []
answer = 0
for _ in range(n):
    P, L = map(int, sys.stdin.readline().split())
    mileages = list(map(int, sys.stdin.readline().split()))
    heapq.heapify(mileages)
    num = L-P
    if num > 0:
        heapq.heappush(candidates, 1)
    else:
        for _ in range(abs(num)):
            heapq.heappop(mileages)
        heapq.heappush(candidates, heapq.heappop(mileages))

while candidates:
    mileage = heapq.heappop(candidates)
    if m - mileage >= 0:
        answer += 1
        m -= mileage
    else: 
        break
print(answer)