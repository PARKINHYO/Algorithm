import sys
from typing import List
input = sys.stdin.readline
class Solution:
    def leaf(self, N: int, tree: List[int], k: int):
        def dfs(k, tree):
            
            """tree리스트에서 지울 노드쪽을 
            의미 없는 -2로 바꿔준다. """
            tree[k] = -2
            
            for i in range(len(tree)):
                
                """k를 부모노드로 가지는 
                i(자식노드)를 찾아서 dfs를 호출하면
                자식노드 쭈루룩 다 -2로 바뀌고 dfs 종료됨"""
                if k == tree[i]:
                    dfs(i, tree)
        
        # 지울 노드와 노드의 부모리스트로 dfs 호출
        dfs(k, tree)
        
        
        count = 0
        
        """이젠 for문으로 tree리스트를 인덱스(트리노드)를 
        기준으로 해서 돌면서 -2면은 지울노드 및 지울노드의 
        자식노드들이므로 다 넘어가고, 트리노드가 트리의 
        값(부모노드)에 없으면 count를 1 증가시킴"""
        for i in range(len(tree)):
            if tree[i] != -2 and i not in tree:
                count += 1
        return count

N = int(input())
tree = list(map(int, input().split()))
k = int(input())
print(Solution().leaf(N, tree, k))