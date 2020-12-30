

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:

            # 리프노드의 left, right 노드를 None으로 초기화하므로 거기까지 타고 갔을때 -1을 리턴됨.
            if not node:
                return -1

            # 리프노트 다음 가상노드까지 끝까지 타고 들어감
            left = dfs(node.left)
            right = dfs(node.right)

            # 왼쪽, 오른쪽 상태값에 2를 더해서 거리를 구함. 기존 거리에 누적으로 max 값을 측정.
            self.longest = max(self.longest, left + right + 2)

            # 아들 노드에 1더해서 상태값 리턴.
            return max(left, right) + 1
        dfs(root)

        return self.longest

