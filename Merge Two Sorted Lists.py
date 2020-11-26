from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        cur = dummy_head
        while l1 is not None or l2 is not None:
            if l1 is None:
                cur.next = l2
                return dummy_head.next
            elif l2 is None:
                cur.next = l1
                return dummy_head.next
            elif l2.val < l1.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = None
        return dummy_head.next


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
print_list(test.mergeTwoLists(array_to_list([1]), array_to_list([1])))
print_list(test.mergeTwoLists(array_to_list([1, 2, 4]), array_to_list([1, 3, 4])))
