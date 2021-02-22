from typing import List


class Solution:
    def validParenthesis(self, T: int, L: List[str]) -> List[str]:
        par = {")": "("}
        answer = []
        for i in range(T):
            stack = []
            isvalid = True
            for j in range(len(L[i])):
                if L[i][j] == "(":
                    stack.append("(")
                elif not stack or par[")"] != stack.pop():
                    isvalid = False
                    break

            if isvalid and not stack:
                answer.append("YES")
            else:
                answer.append("NO")
        return answer


T = int(input())
answers = Solution().validParenthesis(T, [input() for x in range(T)])
for answer in answers:
    print(answer)
