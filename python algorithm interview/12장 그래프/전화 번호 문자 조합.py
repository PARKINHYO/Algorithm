from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                print(result)
                print("return")
                print()
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    print(f'i : {i}, j: {j}, dfs({i+1}, {path+j})')
                    dfs(i + 1, path + j)

        if not digits:
            return []

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result


Solution().letterCombinations("23")

