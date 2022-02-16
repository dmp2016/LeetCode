from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev = dummy
        while head and head.next:
            next = head.next
            prev.next = next
            next.next, head.next = head, next.next
            prev = head
            head = head.next
        return dummy.next


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
print_list(test.swapPairs(array_to_list([1, 2, 3, 4])))
print_list(test.swapPairs(array_to_list([1])))
print_list(test.swapPairs(array_to_list([])))
print_list(test.swapPairs(array_to_list([1, 2, 3, 4, 5])))
