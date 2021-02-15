"""
fixme
 https://leetcode.com/problems/reverse-linked-list/
 Q15. 역순 연결 리스트
 연결 리스트를 뒤집어라.
 입력 : 1 → 2 → 3 → 4 → 5 → NULL
 출력 : 5 → 4 → 3 → 2 → 1 → NULL
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseListRecur(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            print(prev.val)
            return reverse(next, node)

        return reverse(head)

    def reverseListList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev


Solution().reverseListRecur(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))




