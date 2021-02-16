"""
fixme
 https://leetcode.com/problems/reverse-linked-list-ii/
 Q19. 역순 연결 리스트Ⅱ
 인덱스 m에서 n까지를 역순으로 ㅁ나들어라. 인덱스 m은 1부터 시작한다.
 입력 1 → 2 → 3 → 4 → 5 → NULL, m = 2, n = 4
 출력 1 → 4 → 3 → 2 → 5 → NULL
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(m - 1):
            start = start.next

        end = start.next

        for _ in range(n - m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
