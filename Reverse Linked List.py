from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            tmp_next = head.next
            head.next = prev
            prev = head
            head = tmp_next
        return prev


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
print_list(test.reverseList(array_to_list([1, 2, 3, 4, 5])))
print_list(test.reverseList(array_to_list([1, 2])))
print_list(test.reverseList(array_to_list([])))
