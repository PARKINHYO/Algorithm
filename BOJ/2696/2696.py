from sys import stdin
from typing import List


class Solution:
    def centerValue(self, M: int, data: List[int]):

        left = 0
        answers = []
        for right in range(1, M + 1, 2):
            suffix = data[left:right]
            suffix.sort()
            answers.append(suffix[left + (right - left) // 2])

        if len(answers) <= 10:
            print(len(answers))
            print(answers)
        else:
            count = 0
            for answer in answers:
                if count == 10:
                    print()
                    count = 0
                print(answer, end=" ")
                count += 1

        return


for _ in range(int(stdin.readline())):
    M = int(stdin.readline())
    Solution().centerValue(M, list(map(int, stdin.readline().split())))
