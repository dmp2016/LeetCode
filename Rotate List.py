from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        n = 0
        tmp_head = head
        last = tmp_head
        while tmp_head:
            n += 1
            last = tmp_head
            tmp_head = tmp_head.next
        k %= n
        k = n - k
        tmp_head = head
        for _ in range(k - 1):
            tmp_head = tmp_head.next
        last.next = head
        new_head = tmp_head.next
        tmp_head.next = None
        return new_head


def array_to_list(list: List) -> ListNode:
    item = None
    for v in list[::-1]:
        item = ListNode(v, item)
    return item


def print_list(head: ListNode):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()


test = Solution()
print_list(test.rotateRight(None, 10))
print_list(test.rotateRight(array_to_list([1]), 10))
print_list(test.rotateRight(array_to_list([1, 2, 3, 4, ]), 1))
print_list(test.rotateRight(array_to_list([1, 2, 3, 4, ]), 2))
