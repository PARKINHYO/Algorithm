from sys import stdin


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []
        parent.append(0)
        rank.append(0)

        for node in range(1, self.V+1):
            parent.append(node)
            rank.append(0)
        print(parent)

        while e < self.V - 1:

            u, v, w = self.graph[i]

            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:

                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        answer = 0
        for u, v, weight in result:
            answer += weight
        print(answer)


if __name__ == '__main__':
    V, E = map(int, stdin.readline().split(" "))
    g = Graph(V)
    for i in range(E):
        u, v, w = map(int, stdin.readline().split(" "))
        g.addEdge(u, v, w)

    g.KruskalMST()
