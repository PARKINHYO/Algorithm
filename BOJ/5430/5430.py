from sys import stdin
from typing import List
from collections import deque


class Solution:
    def AC(self, p: str, n: int, data: List[str]):
        queue = deque(data)
        reverseFlag = 0
        errorFlag = 0
        for func in p:
            if func == "R":
                if reverseFlag == 0:
                    reverseFlag = 1
                else:
                    reverseFlag = 0
            else:
                if queue:
                    if reverseFlag == 0:
                        queue.popleft()
                    else:
                        queue.pop()
                else:
                    errorFlag = 1
                    break
        if errorFlag == 1:
            print("error")
        else:
            if reverseFlag == 1:
                queue.reverse()
            print("[", ",".join(list(queue)), "]", sep="")

        return


for _ in range(int(stdin.readline())):
    p = input()
    n = int(stdin.readline())
    if n == 0:
        if "D" in p:
            input()
            print("error")
        else:
            input()
            print("[]")
    else:
        tmp = input()
        data = list(tmp[1:len(tmp) - 1].split(","))
        Solution().AC(p, n, data)
