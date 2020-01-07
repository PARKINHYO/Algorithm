from sys import stdin
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        self.answer = []
        self.before = 0


    def addEdge(self, u, v):

        self.graph[u].append(v)

    def isEdge(self, u, v):
        for i in self.graph[u]:
            if i == v:
                return True

        return False

    def DFSUtil(self, v, visited):

        visited[v] = True

        self.answer.append(v)

        for i in self.graph[v]:

            if visited[i] == False:
                self.DFSUtil(i, visited)


    def DFS(self, v):

        visited = [False] * 105
        self.DFSUtil(v, visited)

        return self.answer

if __name__ == '__main__':
    V = int(stdin.readline())
    g = Graph(V)
    for i in range(V):
        E = list(map(int, stdin.readline().split(" ")))
        for j in range(V):
            if E[j] == 1:

                g.addEdge(i, j)

    answer = []

    for i in range(0, V):

        tmpAnswer = g.DFS(i)
        tmpAnswer2 = [0]*V
        for j in tmpAnswer:
            tmpAnswer2[j] = 1
            if i == j:
                tmpAnswer2[j] = 0

        for j in tmpAnswer:
            tmp = g.isEdge(j, i)
            if tmp == True:
                tmpAnswer2[i] = 1

        answer.append(tmpAnswer2)
        while len(tmpAnswer) > 0 : tmpAnswer.pop()

    for i in range(len(answer)):
        for j in range(len(answer)):
            print(answer[i][j], end="")
            if j == len(answer)-1:
                pass
            else:
                print(" ", end="")
        print()
