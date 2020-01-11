from collections import defaultdict
from sys import stdin


class Graph():

    def __init__(self):

        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

    def BFS(self, s):

        visited = [False] * 10005
        depth = [0] * 10005
        queue = []

        queue.append(s)
        depth[s] = 1
        visited[s] = True

        while queue:

            s = queue.pop(0)
            # print(s, end=" ")
            # print(depth[s], end=" ")
            # print()

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    depth[i] = depth[s] + 1
                    visited[i] = True

        return depth[max(self.graph)]


if __name__ == '__main__':

    # f = open('input.txt', 'r')
    # file_txt = []
    # for line in f:
    #     file_txt.append(line[:-1])
    # f.close()

    g = Graph()

    N, M = map(int, stdin.readline().split(" "))

    MAP = []
    for i in range(N):
        tmp = stdin.readline()
        MAP.append(tmp[:-1])

    count = 1
    for i in range(N):
        for j in range(M):

            if MAP[i][j] == "1":

                if j + 1 < M:
                    if MAP[i][j + 1] == "1":
                        g.addEdge(count, count + 1)
                        # print(count, count + 1)

                if j - 1 >= 0:
                    if MAP[i][j - 1] == "1":
                        g.addEdge(count, count - 1)
                        # print(count, count - 1)

                if i + 1 < N:
                    if MAP[i + 1][j] == "1":
                        g.addEdge(count, count + M)
                        # print(count, count + M)

                if i - 1 >= 0:
                    if MAP[i - 1][j] == "1":
                        g.addEdge(count, count - M)
                        # print(count, count - M)

            else:
                pass

            count += 1

    # for i in range(N):
    #     for j in range(N):
    #         if i == j:
    #             pass
    #         if i > j:
    #             if file_txt[i + 1][j] == "1":
    #                 g.addEdge(j + 1, i + 1)

    answer = g.BFS(1)
    # print()
    print(answer, end="")
