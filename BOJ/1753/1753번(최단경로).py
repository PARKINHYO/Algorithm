import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist, sptSet):
        for node in range(self.V):
            if sptSet[node] == False:
                print("INF")
            else:
                print(dist[node])


    def minDistance(self, dist, sptSet):
        min = 200000
        min_index = 0

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [200000] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:

                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist, sptSet)

if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().split(" "))
    K = int(sys.stdin.readline())
    g = Graph(V)

    for i in range(E):
        u, v, w = map(int, sys.stdin.readline().split(" "))
        g.graph[u-1][v-1] = w

    g.dijkstra(K-1)

