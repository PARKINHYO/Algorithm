import sys, collections
from typing import List
input = sys.stdin.readline


class Solution:
    def fourth_dot(self, coordinates: List[List[int]]):
        left = collections.defaultdict(int)
        right = collections.defaultdict(int)
        for coordinate in coordinates:
            left[coordinate[0]] += 1
            right[coordinate[1]] += 1
        answer = []
        for key in left.keys():
            if left[key] == 1:
                answer.append(key)
        for key in right.keys():
            if right[key] == 1:
                answer.append(key)
                
        
        return answer


coordinates = []
for _ in range(3):
    coordinates.append(list(map(int, input().split())))
print(*Solution().fourth_dot(coordinates))

