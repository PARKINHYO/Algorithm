from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
               return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)


            return True


        for x in list(graph):
            if not dfs(x):
                return False


        return True


print(Solution().canFinish(2, [[0,1], [0,2], [1,2]]))