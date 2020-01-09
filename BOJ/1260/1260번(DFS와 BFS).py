from collections import defaultdict
from sys import stdin

class Graph():

    def __init__(self):

        self.graph = defaultdict(list)
        self.answer = []

    def addEdge(self, u, v):

        self.graph[u].append(v)
        self.graph[u].sort()

    def BFS(self, s):

        visited = [False]* 1005
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            s = queue.pop(0)
            self.answer.append(s)

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return self.answer

    def DFSUtil(self, v, visited):

        visited[v] = True
        self.answer.append(v)



        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, v):

        visited = [False] * 1005
        self.DFSUtil(v, visited)

        return self.answer


if __name__ == '__main__':

    bfs = Graph()
    dfs = Graph()

    N, M, V = map(int, stdin.readline().split(" "))

    for i in range(M):
        u, v = map(int, stdin.readline().split(" "))
        bfs.addEdge(u, v)
        bfs.addEdge(v, u)
        dfs.addEdge(u, v)
        dfs.addEdge(v, u)



    answer1 = dfs.DFS(V)
    answer2 = bfs.BFS(V)

    for i in range(len(answer1)):
        if i == len(answer1)-1:
            print(answer1[i])
        else:
            print(answer1[i], end=" ")

    for i in range(len(answer2)):
        if i == len(answer2)-1:
            print(answer2[i])
        else:
            print(answer2[i], end=" ")


