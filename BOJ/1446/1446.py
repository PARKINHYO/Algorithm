import sys

N, D = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 지름길 없을 때 전체 거리
dis = [i for i in range(D+1)]


for i in range(D+1):
    if i > 0:
        # 지름길이 사실 더 멀수도 있어서 계속 전꺼 + 1이랑 비교해서 업데이트 해줌. 
        dis[i] = min(dis[i], dis[i-1] + 1)
    for s, e, d in li:
        # 지름길에 도착하면 거리 지름길로 업데이트 시켜줌. 
        if i == s and e <= D and dis[i] + d < dis[e]:
            dis[e] = dis[i] + d
print(dis[D])
