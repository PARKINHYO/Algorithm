import sys
from typing import List
input = sys.stdin.readline


class Solution:
    def arbeit(self, n: int, m: int, pay: List[int]):
        if n == 0 or m == 0:
            return 0
        left, right = 0, m
        answer = sum(pay[left: right])
        cur = answer
        while right < n:
            cur += pay[right]
            cur -= pay[left]
            if cur > answer:
                answer = cur
            left += 1
            right += 1
        return answer


n, m = map(int, input().split())
print(Solution().arbeit(n , m, list(map(int, input().split()))))