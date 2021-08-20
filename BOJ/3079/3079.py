import sys
from typing import List
input = sys.stdin.readline


class Solution:
    def immigration(self, N: int, M: int, time: List[int]) -> int:
        tmp = M//N
        if M % N:
            tmp += 1
        start = 0
        end = max(time)*tmp
        while start <= end:
            mid = (start + end) // 2
            count = 0
            check = False
            for t in time:
                count += mid//t
                if count >= M:
                    check = True
                    break
            if check:
                end = mid - 1
            else:
                start = mid + 1
                
        return max(start, end)


N, M = map(int, input().split())
print(Solution().immigration(N, M, [int(input()) for _ in range(N)]))
