import sys
from sys import stdin


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent):
        answer = 0
        for i in range(1, self.V):
            answer += self.graph[i][parent[i]]

        print(answer)

    def minKey(self, key, mstSet):
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V

        key[0] = 0
        mstSet= [False] * self.V
        parent[0] = -1

        for cout in range(self.V):

            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


if __name__ == '__main__':

    N = int(stdin.readline())
    M = int(stdin.readline())

    g = Graph(N)
    for i in range(M):
        a, b, c = map(int, stdin.readline().split(" "))
        g.graph[a-1][b-1] = c
        g.graph[b-1][a-1] = c

    g.primMST()

