from typing import List
import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                print(f'graph[stack[-1]: {graph[stack[-1]]}')
                stack.append(graph[stack[-1]].pop(0))
                print(f'stack : {stack}')
            print(f'route : {route}')
            route.append(stack.pop())

        return route[::-1]

print(Solution().findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))

