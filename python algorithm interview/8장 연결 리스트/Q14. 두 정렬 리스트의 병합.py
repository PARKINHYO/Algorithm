"""
fixme
 https://leetcode.com/problems/merge-two-sorted-lists/
 Q14. 두 정렬 리스트의 병합
 정렬되어 있는 두 연결 리스트를 합쳐라 .
 입력 : 1 → 2 → 4, 1 → 3 → 4
 출력 : 1 → 1 → 3 → 4 → 4
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
Solution().mergeTwoLists(l1, l2)
