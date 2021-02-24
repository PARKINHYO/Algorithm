from typing import List
import collections
from sys import stdin

class Solution:
    def printerQueue(self, docCount: int, docIndex: int, priority: List[int]) -> int:
        printer = collections.deque()
        for i, p in enumerate(priority):
            printer.append([i, p])
        answer = 0
        while printer:
            i, p = printer.popleft()
            if p == max(priority):
                answer += 1
                if i == docIndex:
                    return answer
                else:
                    priority.remove(p)
            else:
                printer.append([i, p])


for i in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    priority = list(map(int, stdin.readline().split()))
    print(Solution().printerQueue(N, M, priority))