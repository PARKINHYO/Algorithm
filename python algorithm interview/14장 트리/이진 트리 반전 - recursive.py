

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:

            # 릿코드 예제에서 2, 7이 스왑될 때, 2, 7 밑의 자식 노드가 다 붙어 있으므로 같이 스왑되서 전체 반전됨.
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None
