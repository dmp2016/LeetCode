from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dump = ListNode(None, head)
        cur_ins = dump
        prev = dump
        while head:
            if head.val < x:
                if head != cur_ins.next:
                    next = head.next
                    prev.next = next
                    head.next = cur_ins.next
                    cur_ins.next = head
                    cur_ins = head
                    head = next
                else:
                    cur_ins = head
                    prev, head = head, head.next
            else:                
                prev, head = head, head.next
        return dump.next


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
print_list(test.partition(head=array_to_list([1, 4, 3, 2, 5, 2]), x=3))
print_list(test.partition(head=array_to_list([2, 1]), x=2))
print_list(test.partition(head=array_to_list([1, 2]), x=2))
print_list(test.partition(head=array_to_list([1, 2]), x=1))
print_list(test.partition(head=array_to_list([1, 2]), x=3))
print_list(test.partition(head=array_to_list([1]), x=1))
print_list(test.partition(head=array_to_list([1]), x=2))
print_list(test.partition(head=array_to_list([2]), x=1))
