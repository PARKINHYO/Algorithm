import sys
from typing import List
input = sys.stdin.readline


class Solution:
    def validation(self, numbers: List[int]):
        answer = 0
        for number in numbers:
            answer += (number ** 2)
        return answer % 10

print(Solution().validation(list(map(int, input().split()))))
    

