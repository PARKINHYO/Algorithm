from sys import stdin
from typing import List
from collections import defaultdict


class Solution:
    def fashionKing(self, clothes: List[List[str]]):
        myDict = defaultdict(int)
        for a, b in clothes:
            myDict[b] += 1
        answer = 1
        for key in myDict.keys():
            answer *= (myDict[key] + 1)
        print(answer - 1)


answer = []
for _ in range(int(stdin.readline())):
    clothes = []
    for _ in range(int(stdin.readline())):
        clothes.append(input().split())
    Solution().fashionKing(clothes)
