from sys import stdin
from collections import defaultdict

class Graph:
    def __init__(self):

        self.graph = defaultdict(list)
        self.count = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        self.count +=1


        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, v):

        visited = [False] * 105

        self.DFSUtil(v, visited)

        return self.count



if __name__ == '__main__':
    g = Graph()

    COM = int(stdin.readline())
    N = int(stdin.readline())
    for i in range(N):
        edge = list(map(int, stdin.readline().split(" ")))
        g.addEdge(edge[0], edge[1])
        g.addEdge(edge[1], edge[0])

    answer = g.DFS(1) - 1
    print(answer)



