from collections import defaultdict
from sys import stdin


class Graph():

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

    def BFS(self, vertices):

        apart = []
        apartCount = 0

        visited = [False] * 630
        queue = []

        for i in range(len(vertices)):

            if visited[vertices[i]] == False:
                visited[vertices[i]] = True
                queue.append(vertices[i])
                apartCount += 1
            else:
                continue

            tmp = 0
            while queue:
                s = queue.pop(0)
                tmp += 1
                for i in self.graph[s]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True

            apart.append(tmp)

        print(apartCount)
        apart.sort()
        for i in apart:
            print(i)


def Input():
    N = int(stdin.readline())
    g = Graph()

    MAP = []
    for i in range(N):
        tmp = stdin.readline()
        MAP.append(tmp[:-1])

    count = 1
    vertex = []
    for i in range(N):
        for j in range(N):

            if MAP[i][j] == "1":
                vertex.append(count)
                if j + 1 < N:
                    if MAP[i][j + 1] == "1":
                        g.addEdge(count, count + 1)
                        # print(count, count + 1)

                if j - 1 >= 0:
                    if MAP[i][j - 1] == "1":
                        g.addEdge(count, count - 1)
                        # print(count, count - 1)

                if i + 1 < N:
                    if MAP[i + 1][j] == "1":
                        g.addEdge(count, count + N)
                        # print(count, count + N)

                if i - 1 >= 0:
                    if MAP[i - 1][j] == "1":
                        g.addEdge(count, count - N)
                        # print(count, count - N)

            else:
                pass

            count += 1

    vertex.sort()

    g.BFS(vertex)


if __name__ == '__main__':
    Input()
