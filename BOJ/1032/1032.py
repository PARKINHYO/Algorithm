from typing import List


class Solution:
    def prompt(self, N: int, files: List[str]):
        answer = ''
        for i in range(len(files[0])):
            comp = files[0][i]
            isSame = True
            for j in range(N):
                if comp != files[j][i]:
                    isSame = False
            if isSame:
                answer += files[0][i]
            else:
                answer += '?'
        print(answer)

N = int(input())
files = [input() for i in range(N)]
Solution().prompt(N, files)
