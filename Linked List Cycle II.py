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
                    head2 = head2.next
                    if head2 == head1:
                        break
                    cnt += 1
                break

        def check_cycle(head: Optional[ListNode]) -> bool:
            tmp = head
            for _ in range(cnt + 1):
                tmp = tmp.next
            return tmp == head

        left = 0
        right = 10000

        while left < right - 1:
            mid = (left + right) // 2
            tmp = head
            for _ in range(mid):
                tmp = tmp.next
            if check_cycle(tmp):
                left = mid
            else:
                right = mid
        tmp = head
        for _ in range(mid):
            tmp = tmp.next
        return tmp


def array_to_list(list: List, pos: int) -> ListNode:
    item = None
    for v in list[::-1]:
        item = ListNode(v, item)
    return item


test = Solution()
data = array_to_list([1, 2, 3, 4, 5])
head = data
head = head.next

