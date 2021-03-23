from sys import stdin
from typing import List


class Solution:
    def zero(self, monies: List[int]):
        stack = []

        for money in monies:
            if money == 0:
                stack.pop()
                continue
            stack.append(money)
        print(sum(stack))


K = int(stdin.readline())
monies = []
for i in range(K):
    monies.append(int(stdin.readline()))
Solution().zero(monies)
