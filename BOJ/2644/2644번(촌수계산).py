from collections import defaultdict
from sys import stdin

class Graph():

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s, v):


        visited = [False] * 105
        queue = []
        result = [0]* 105

        queue.append(s)
        visited[s] = True



        while queue:

            s = queue.pop(0)


            for i in self.graph[s]:

                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    result[i] = result[s] + 1

        if result[v] == 0:
            print(-1)
        else:
            print(result[v])



if __name__ == '__main__':

    g = Graph()

    # f = open('input.txt', 'r')
    # file_txt = []
    # for line in f:
    #
    #     file_txt.append(line[:-1])
    # f.close()
    n = int(stdin.readline())
    a, b = map(int, stdin.readline().split(" "))
    m = int(stdin.readline())

    for i in range(m):
        tmp1, tmp2 = map(int, stdin.readline().split(" "))
        g.addEdge(tmp1, tmp2)

    g.BFS(a, b)


