import sys
import collections
import heapq
from typing import List
input = sys.stdin.readline


class Solution:
    def line(self, N: int, M: int,
             compare: List[List[int]], degree: List[int]):
        heap = []
        for i in range(1, N+1):
            if degree[i] == 0:
                heapq.heappush(heap, i)
        answer = []
        while heap:
            student = heapq.heappop(heap)
            answer.append(student)
            for v in compare[student]:
                degree[v] -= 1
                if degree[v] == 0:
                    heapq.heappush(heap, v)
        return answer


N, M = map(int, input().split())
compare = collections.defaultdict(list)
degree = collections.defaultdict(int)
for _ in range(M):
    a, b = map(int, input().split())
    compare[a].append(b)
    degree[b] += 1
print(*Solution().line(N, M, compare, degree))
