import sys
from typing import List
input = sys.stdin.readline

class Solution: 
    def memorization_king(self, N: int, note_one: List[int], 
                          M: int, note_two: List[int]):
        for v in note_two:
            if v in note_one:
                print(1)
            else:
                print(0)
    

for _ in range(int(input())):
    N = int(input())
    note_one = set(map(int, input().split()))
    M = int(input())
    note_two = list(map(int, input().split()))
    Solution().memorization_king(N, note_one, M, note_two)
    