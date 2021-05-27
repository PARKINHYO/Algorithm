import sys
import copy
import collections
sys.setrecursionlimit(10**6)


def sol(graph, N):
    def dfs(i,j):
        if visited[i][j]:
            return
        visited[i][j] = True
        for index in range(4):
            newx = x[index] + i
            newy = y[index] + j
            if 0<= newx < color[1] and 0 <= newy < color[1]:
                if graph[newx][newy] == color[0]:
                    dfs(newx,newy)
        
        return
    visited = [[False]*N for _ in range(N)]
    color = [0,N]
    count = 0
    x = [-1,1,0,0]
    y = [0,0,-1,1]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                color[0] = graph[i][j]
                dfs(i, j)
                count += 1
    return count
    
    


N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(sys.stdin.readline().rstrip())
rg_graph = copy.deepcopy(graph)
for i in range(N):
    for j in range(N):
        if rg_graph[i][j] == 'R':
            rg_graph[i] = rg_graph[i][:j] + 'G' + rg_graph[i][j+1:]

print(sol(graph, N))
print(sol(rg_graph, N))
