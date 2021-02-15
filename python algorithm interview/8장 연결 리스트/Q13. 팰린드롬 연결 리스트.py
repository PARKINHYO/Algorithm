"""
fixme
 https://leetcode.com/problems/palindrome-linked-list/
 Q13. 팰린드롬 연결 리스트
 연결 리스트가 팰린드롬 구조인지 판별하라.
 입력 : 1 → 2
 출력 : False
 입력 : 1 → 2 → 2 → 1
 출력 : True
"""

from typing import List, Deque
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def isPalindromeList(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

    def isPalindromeDeque(self, head: ListNode) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    def isPalindromeRunner(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev


if __name__ == '__main__':
    print(Solution().isPalindromeRunner(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
