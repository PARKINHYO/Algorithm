from sys import stdin
from typing import List


class Solution:
    def centerValue(self, M: int, data: List[int]):

        answers = []
        for right in range(1, M + 1, 2):
            suffix = data[:right]
            suffix.sort()
            answers.append(suffix[right // 2])

        if len(answers) <= 10:
            print(len(answers)) 
            print(*answers)
        else:
            print(len(answers))
            linedAnswers = []
            tmp = []
            for answer in answers:
                if len(tmp) == 10:
                    linedAnswers.append(tmp)
                    tmp = []
                tmp.append(answer)
            linedAnswers.append(tmp)
            for linedAnswer in linedAnswers:
                print(*linedAnswer)

        return


for _ in range(int(stdin.readline())):
    M = int(stdin.readline())

    if M <= 10:
        Solution().centerValue(M, list(map(int, stdin.readline().split())))
    else:
        data = []
        a = M // 10
        b = M % 10
        if b == 0:
            for i in range(a):
                data.extend(list(map(int, stdin.readline().split())))
            Solution().centerValue(M, data)
        else:
            for i in range(a+1):
                data.extend(map(int, stdin.readline().split()))
            Solution().centerValue(M, data) 
