import sys
input = sys.stdin.readline


class Solution:
    def R2(self, R: int, S: int):
        return S*2-R
    

R, S = map(int, input().split())
print(Solution().R2(R, S))