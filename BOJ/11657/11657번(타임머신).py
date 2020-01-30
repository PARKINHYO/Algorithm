from sys import stdin

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        for i in range(1, self.V):
            if dist[i] == float("Inf"):
                print(-1)
            else:
                print(dist[i])

    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("-1")
                return

        self.printArr(dist)



if __name__ == '__main__':

    N, M = map(int, stdin.readline().split(" "))
    g = Graph(N)
    for i in range(M):
        A, B, C = map(int, stdin.readline().split(" "))
        g.addEdge(A-1, B-1, C)

    g.BellmanFord(0)
