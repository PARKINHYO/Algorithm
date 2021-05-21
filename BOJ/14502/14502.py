import sys
import itertools
import copy
import collections


def bfs(i, j):
    queue = collections.deque()
    queue.append((i, j))
    while queue:
        popx, popy = queue.popleft()
        if not visited[popx][popy]:
            visited[popx][popy] = True
            
            # 좌표 돌아가며 추가할지 결정
            for i in range(4):
                newx = popx + x[i]
                newy = popy + y[i]
                if 0 <= newx < N and 0 <= newy < M:
                    if test_graph[newx][newy] == 0:
                        test_graph[newx][newy] = 2
                        queue.append((newx, newy))
    return


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 0인 좌표를 다 저장
emptyloc = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            emptyloc.append((i, j))

# 0인 좌표중 3개 조합
three_walls = list(itertools.combinations(emptyloc, 3))

# 위, 아래 , 오, 왼
x = [0, 0, 1, -1]
y = [1, -1, 0, 0]

answer = 0
for three_wall in three_walls:
    # 기존 그래프 복사 후
    test_graph = copy.deepcopy(graph)

    # 조합한 3개 좌표에 1넣고,
    for i, j in three_wall:
        test_graph[i][j] = 1
        
    # 2일 때 bfs 돌려서 양옆위아래 돌리면서 2채운다.
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if test_graph[i][j] == 2:
                bfs(i, j)
                
    # bfs 다돌린 바이러스 걸린 그래프에서 비어있는 0의 개수 찾기
    tmp = 0
    for line in test_graph:
        tmp += line.count(0)

    answer = max(answer, tmp)
print(answer)
