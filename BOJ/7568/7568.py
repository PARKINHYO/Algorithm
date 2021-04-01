from typing import List


class Solution:
    def getScore(self, info: List[List[int]]):
        for i in info:
            rank = 1
            for j in info:
                if i[0] < j[0] and i[1] < j[1]:
                    rank += 1
            print(rank, end=" ")


info = []
for i in range(int(input())):
    info.append(list(map(int, input().split())))
Solution().getScore(info)
