import sys
import collections
input = sys.stdin.readline

N, K = map(int, input().split())
Q = collections.deque([(N, 0)])
visited = [False]*100001
while Q:
    loc, count = Q.popleft()
    if loc == K:
        print(count)
        break
    if not visited[loc]:
        visited[loc] = True
        if 0<= (2*loc) <= 100000:
            # 순간이동 비용 0이라서 appendleft()
            Q.appendleft((2*loc, count))
        if 0<= (loc+1) <= 100000:
            Q.append((loc+1, count+1))
        if 0<= (loc-1) <= 100000:
            Q.append((loc-1, count+1))



