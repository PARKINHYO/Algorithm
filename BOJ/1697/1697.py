from collections import deque
from sys import stdin

class Solution:
    def hide(self, N: int, K: int) -> int:
        c = 0
        queue = deque([[N, c]])
        visited = [False] * 100001
        while queue:
            l, c = queue.popleft()
            if not visited[l]:
                visited[l] = True
                if l == K:
                    return c
                c += 1
                if l * 2 <= 100000:
                    queue.append([l * 2, c])
                if l + 1 <= 100000:
                    queue.append([l + 1, c])
                if l - 1 >= 0:
                    queue.append([l - 1, c])
        return c

N, K = map(int, stdin.readline().split())
print(Solution().hide(N, K))
