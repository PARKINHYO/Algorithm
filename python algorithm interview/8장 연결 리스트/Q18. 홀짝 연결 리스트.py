"""
fixme
 https://leetcode.com/problems/odd-even-linked-list/
 Q18. 홀짝 연결 리스트
 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.
 입력 : 1 → 2 → 3 → 4 → 5 → NULL
 출력 : 1 → 3 → 5 → 2 → 4 → NULL
 입력 : 2 → 1 → 3 → 5 → 6 → 4 → 7 → NULL
 출력 : 2 → 3 → 6 → 7 → 1 → 5 → 4 → NULL
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode):
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head
