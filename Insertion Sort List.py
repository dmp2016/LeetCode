from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        cur = head.next
        head.next = None
        while cur is not None:
            cur_next = cur.next
            cur.next = None
            if head.val >= cur.val:
                cur.next, head = head, cur
            else:
                tmp = head
                while tmp is not None and tmp.val < cur.val:
                    tmp_prev, tmp = tmp, tmp.next
                tmp_prev.next, cur.next = cur, tmp
            cur = cur_next
        return head


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
print_list(test.insertionSortList(array_to_list([4, 2, 1, 3])))
print_list(test.insertionSortList(array_to_list([-1, 5, 3, 4, 0])))
print_list(test.insertionSortList(array_to_list([1, 2, 3, 4])))
