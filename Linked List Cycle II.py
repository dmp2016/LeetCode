from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head1 = head2 = head

        while True:
            if not head1:
                return None
            head1 = head1.next
            if not head2:
                return None
            head2 = head2.next
            if not head2:
                return None
            head2 = head2.next
            if head1 and head1 == head2:
                cnt = 0
                while True:
                    cnt += 1
                    head2 = head2.next
                    if head2 == head1:
                        break
                break

        def check_cycle(head: Optional[ListNode]) -> bool:
            tmp = head
            for _ in range(cnt):
                tmp = tmp.next
            return tmp == head

        left = -1
        right = 10000

        while left < right - 1:
            mid = (left + right) // 2
            tmp = head
            for _ in range(mid):
                tmp = tmp.next
            if check_cycle(tmp):
                right = mid
            else:
                left = mid
        tmp = head
        for _ in range(right):
            tmp = tmp.next
        return tmp
