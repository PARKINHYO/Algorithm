from sys import stdin
from collections import defaultdict


class Graph():

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):

        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited[v] = True


        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self):

        visited = [False] * 100000

        count = 0
        for i in range(1, self.V + 1):
            if visited[i] == False:
                count += 1
                self.DFSUtil(i, visited)

        return count


if __name__ == '__main__':
    VE = list(map(int, stdin.readline().split(" ")))
    g = Graph(VE[0])
    for i in range(VE[1]):
        tmp = list(map(int, stdin.readline().split(" ")))
        g.addEdge(tmp[0], tmp[1])
        g.addEdge(tmp[1], tmp[0])

    print(g.DFS())
