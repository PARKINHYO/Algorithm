from typing import List


class Solution:
    def whiteBlock(self, map: List[str]):
        answer = 0
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        if map[i][j] == 'F':
                            answer += 1
                else:
                    if j % 2 == 1:
                        if map[i][j] == 'F':
                            answer += 1
        print(answer)


map = [input() for i in range(8)]
Solution().whiteBlock(map)
