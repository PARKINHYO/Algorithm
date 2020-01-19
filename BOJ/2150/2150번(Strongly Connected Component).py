from collections import defaultdict
from sys import stdin

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited, answer):

        visited[v] = True
        answer.append(v)

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited, answer)

    def fileOrder(self, v, visited, stack):
        visited[v] = True
        # print("dfs %d" % v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.fileOrder(i, visited, stack)

        stack.append(v)
        # print("stack %d" % v)

    def getTranspose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)

        return g

    def printSCCs(self):

        stack = []
        visited = [False] * 10005

        for i in range(1, self.V+1):
            if visited[i] == False:
                self.fileOrder(i, visited, stack)

        gr = self.getTranspose()

        visited = [False] * 10005
        count = 0
        realAnswer = []
        while stack:
            answer = []
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited, answer)
                realAnswer.append(answer)
                count += 1

        for i in range(len(realAnswer)):
            realAnswer[i].sort()
        realAnswer.sort()
        print(count)
        for i in range(0, len(realAnswer)):
            for j in range(0, len(realAnswer[i])):
                print(realAnswer[i][j], end=" ")
            print("-1")

if __name__ == '__main__':
    V, E = map(int, stdin.readline().split(" "))
    g = Graph(V)
    for i in range(E):
        A, B = map(int, stdin.readline().split(" "))
        g.addEdge(A, B)

    g.printSCCs()
