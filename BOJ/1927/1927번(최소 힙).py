from heapq import heappush, heappop, heapify
from sys import stdin

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insertKey(self, k):
        heappush(self.heap, k)

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while (i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    def extractMin(self):
        return heappop(self.heap)

    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    def getMin(self):
        return self.heap[0]

    def heapLength(self):
        return len(self.heap)


if __name__ == '__main__':

    heapObj = MinHeap()
    N = int(stdin.readline())
    for i in range(N):
        x = int(stdin.readline())
        if x == 0:
            if heapObj.heapLength() == 0:
                print(0)
            else:
                print(heapObj.extractMin())
        else:
            heapObj.insertKey(x)

