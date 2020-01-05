from sys import stdin
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if self.graph[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self):
        answer = [[0] * self.V] * self.V
        visited = [False] * 105
        count = 0

        for i in range(self.V):
            if visited[i] == False:

                self.DFSUtil(i, visited)

                for k in range(len(visited)):
                    if visited[k] == True:
                        count += 1
                if count == self.V:
                    for j in range(len(answer)):
                        answer[i][j] = 1

                else:
                    for j in range(len(answer)):
                        if visited[j] == False:
                            answer[i][j] = 0
                        else:
                            answer[i][j] = 1

                visited = [False] * 105
                count = 0

        return answer


if __name__ == '__main__':
    V = int(stdin.readline())
    g = Graph(V)
    for i in range(V):
        E = list(map(int, stdin.readline().split(" ")))
        for j in range(V):
            if E[j] == 1:
                g.addEdge(i, j)

    print(g.DFS())
