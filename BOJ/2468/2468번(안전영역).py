from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

class graph:

    def __init__(self, V):
        self.graph = defaultdict(list)
        self.weight = defaultdict()
        self.v = V

    def addEdge(self, u, v, w):
        self.graph[u].append(v)
        self.weight[u] = w

    def DFSUtil(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self):

        answers = []

        for i in range(0, 100):
            count = 0
            visited = [False] * 100000

            for j in range(self.v):
                if i >= self.weight[j]:
                    visited[j] = True

            for j in range(self.v):
                if visited[j] == False:
                    count += 1
                    self.DFSUtil(j, visited)
            answers.append(count)
        answers.sort()

        return answers[len(answers)-1]


if __name__ == '__main__':
    n = int(stdin.readline())
    high = []
    G = graph(n * n)
    for i in range(n):
        tmp = list(map(int, stdin.readline().split(" ")))
        high.append(tmp)
    for i in range(n):
        for j in range(n):
            if j + 1 < n:
                G.addEdge(n * i + j, n * i + j + 1, high[i][j])
            if j - 1 >= 0:
                G.addEdge(n * i + j, n * i + j - 1, high[i][j])
            if i + 1 < n:
                G.addEdge(n * i + j, n * (i + 1) + j, high[i][j])
            if i -1 >= 0:
                G.addEdge(n * i + j, n * (i - 1) + j, high[i][j])

    print(G.DFS())

