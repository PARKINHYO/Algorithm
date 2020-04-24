from collections import defaultdict
from sys import stdin
import sys
sys.setrecursionlimit(100000)

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited[v] = True
        # print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, vertices):
        count = 0
        visited = [False] * 2505
        for i in vertices:
            if visited[i] == False:
                # print(i)
                self.DFSUtil(i, visited)
                count += 1
            # print(visited)
        return count


if __name__ == '__main__':

    T = int(stdin.readline())
    for i in range(T):
        M, N, K = map(int, stdin.readline().split())
        xy = [[0] * M for y in range(N)]
        # print(xy)

        for j in range(K):
            x, y = map(int, stdin.readline().split())
            # print(x, y)
            xy[y][x] = 1

        # print(xy)
        g = Graph()
        vertices = set()

        for j in range(N):
            for k in range(M):

                if xy[j][k] == 1:
                    vertices.add(j * M + k)
                    if k + 1 <= M - 1:
                        if xy[j][k + 1] == 1:
                            g.addEdge(M * j + k, M * j + k + 1)
                            # print(M * j + k, M * j + k + 1)

                    if k - 1 >= 0:
                        if xy[j][k - 1] == 1:
                            g.addEdge(M * j + k, M * j + k - 1)
                            # print(M * j + k, M * j + k - 1)

                    if j + 1 <= N - 1:
                        if xy[j + 1][k] == 1:
                            g.addEdge(M * j + k, M * (j + 1) + k)
                            # print(M * j + k, N * (j + 1) + k)

                    if j - 1 >= 0:
                        if xy[j - 1][k] == 1:
                            g.addEdge(M * j + k, M * (j - 1) + k)
                            # print(M * j + k, M * (j - 1) + k)

        print(g.DFS(vertices))

