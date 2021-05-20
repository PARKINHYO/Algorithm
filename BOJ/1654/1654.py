import sys


K, N = map(int, sys.stdin.readline().split())
lans = [int(sys.stdin.readline()) for x in range(K)]
start, end = 1, max(lans)
while start <= end:
    mid = (start + end) // 2
    lines = 0
    for lan in lans: 
        lines += (lan // mid)
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
