from sys import stdin
from collections import defaultdict


class Graph():

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

    def BFS(self, vertices, vertexVisited):

        visited = [False] * 1000005
        queue = []
        depth = [0] * 1000005
        cantTomato = 0

        if vertexVisited == vertices:
            print(0)
            return

        for i in vertexVisited:

            visited[i] = True
            depth[i] = 1
            queue.append(i)

            while queue:

                s = queue.pop(0)

                for j in self.graph[s]:
                    if visited[j] == False:
                        queue.append(j)
                        visited[j] = True
                        depth[j] = depth[s] + 1
            cantTomato += 1

        #fixme 1이 양방향에서 올 때 control해주기

        for i in vertices:
            if visited[i] == False:
                print(-1)
                return
        print(max(depth)-1)
def Input():
    f = open('input.txt', 'r')
    MAP = []
    M, N = map(int, f.readline().split(" "))
    for line in f:
        MAP.append(list(map(int, line.split(" "))))
    f.close()
    print(MAP)

    g = Graph()

    count = 1
    vertices = []
    vertexVisited = []

    for i in range(N):
        for j in range(M):


            if MAP[i][j] == 1:
                vertexVisited.append(count)

            if MAP[i][j] == 1 or MAP[i][j] == 0:
                vertices.append(count)

                if j + 1 < M:
                    if MAP[i][j + 1] == 1 or MAP[i][j + 1] == 0:
                        g.addEdge(count, count + 1)
                        print(count, count + 1)

                if j - 1 >= 0:
                    if MAP[i][j - 1] == 1 or MAP[i][j - 1] == 0:
                        g.addEdge(count, count - 1)
                        print(count, count - 1)

                if i + 1 < N:
                    if MAP[i + 1][j] == 1 or MAP[i + 1][j] == 0:
                        g.addEdge(count, count + M)
                        print(count, count + M)

                if i - 1 >= 0:
                    if MAP[i - 1][j] == 1 or MAP[i - 1][j] == 0:
                        g.addEdge(count, count - M)
                        print(count, count - M)

            count += 1

    print(vertices)
    print(vertexVisited)

    g.BFS(vertices, vertexVisited)


if __name__ == '__main__':
    Input()
