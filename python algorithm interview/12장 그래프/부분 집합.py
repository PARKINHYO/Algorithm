from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(index, path):
            results.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])

        dfs(0, [])
        return results
