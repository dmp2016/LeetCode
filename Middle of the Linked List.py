from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        tmp_head = head
        while tmp_head:
            n += 1
            tmp_head = tmp_head.next
        for _ in range(n // 2):
            head = head.next
        return head

