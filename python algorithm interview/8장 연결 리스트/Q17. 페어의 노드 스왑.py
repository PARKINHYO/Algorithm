"""
fixme.
 https://leetcode.com/problems/swap-nodes-in-pairs/
 Q17. 페어의 노드 스왑
 입력 : 1 → 2 → 3 → 4
 출력 : 2 → 1 → 4 → 3
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairsChageValue(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

    def swapPairsWhile(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head  # fixme [1] 이런식으로 들어오는것을 대비하기 위해 필요
        while head and head.next:
            # fixme b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # fixme prev가 b를 가리키도록 할당
            prev.next = b

            # fixme 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next  # fixme 3, 4가 4, 3으로 바꼈을 때 1, 2 쪽의 2를 4와 연결시키기 위해서는 prev가 꼭 필요하고 매 반복마다 순간 바꿔주어야 한다.

        return root.next

    def swapPairsRecur(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairsRecur(p.next)
            p.next = head
            return p  # fixme if 문에서 종료하게 되면 p를 반환하고 바로 함수가 종료됨
        return head


Solution().swapPairsChageValue(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
