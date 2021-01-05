from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        cur = dummy_head
        while head is not None:
            if head.next is None or head.next.val != head.val:
                cur.next = head
                cur = cur.next
            else:
                while head.next is not None and head.next.val == head.val:
                    head = head.next
            head = head.next
        cur.next = None
        return dummy_head.next


def array_to_list(A: List[int]) -> ListNode:
    head = None
    for n in A[::-1]:
        head = ListNode(n, head)
    return head


def print_list(head: ListNode):
    while head is not None:
        print(head.val, end=', ')
        head = head.next


test = Solution()

print(print_list(test.deleteDuplicates(array_to_list([1,2,3,3,4,4,5]))))
