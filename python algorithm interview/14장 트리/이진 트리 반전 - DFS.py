import collections

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)


        return root

    